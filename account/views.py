from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from .models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm
)
from django.contrib.auth import login, logout, authenticate
from account.forms import (
    RegistrationForm,
    StudentProfileForm,
    EditUserForm,
    EditStudentForm,
)
from django.contrib import messages
from .models import Kolegij
from objava.models import Objava
from django.contrib.auth import update_session_auth_hash #za ponovnu prijavu nakon promjene lozinke!


def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        #ova forma odma provjera postoji li user ili ne, ali ga ne ulogira!
        #tj forma nije validna ako user ne postoji lollllll
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['username'] = form.cleaned_data.get('username')
                    return HttpResponseRedirect(reverse('account:mypage'))
                else:
                     messages.info(request, "Vaš račun je istekao ili je blokiran")

        else:
            messages.info(request, "Pogresan username ili lozinka")

    storage = messages.get_messages(request)
    return render(request, "account/login.html", {'form': form, 'messages':storage})

@login_required()
def settings_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=request.user)
            student_form = EditStudentForm(request.POST, request.FILES, instance=request.user.student)
            if form.is_valid() and student_form.is_valid():
                user_form = form.save()
                student = student_form.save(commit=False)
                student.user = user_form
                student.save()
                return redirect('account:settings')
        else:
            form = EditUserForm(instance=request.user)
            student_form = EditStudentForm(instance=request.user.student)
            student_form.fields['studij'].widget.attrs = {'class': 'form-control'}
            context = {'form': form, 'student_form': student_form}
            return render(request, "account/settings.html", context)

@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            #jedno kad se promjeni lozinka django automatski odjavi usera jer se promjene podaci
            return redirect('account:mypage')
            #neka poruka uspješna promjena blabla
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form' : form}
        return render(request, 'account/change_password.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        student_form = StudentProfileForm(request.POST)
        print('aa')
        print(form.is_valid())
        print(student_form.is_valid())
        if form.is_valid() and student_form.is_valid():
            print('prosao sam')
            user = form.save(commit = False) #prvo spremim podatke iz forme u DJANGO USER MODEL
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Aktiviraj svoj racun'
            message = render_to_string('account/acc_activate.html',
                                       {'user':user, 'domain':current_site.domain,
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                        'token':account_activation_token.make_token(user)})
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            print(student_form.cleaned_data.get('studij'))
            student = student_form.save(commit=False) #želim spremiti u studenta al prvo pohranim podatke (commit - false) i onda nadodam podatke iz usera)
            student.user = user
            student.save()
            return HttpResponse('Confirm')

    form = RegistrationForm()
    student_form = StudentProfileForm()
    student_form.fields['studij'].widget.attrs = {'class': 'form-control'}
    context = {'form' : form, 'student_form' : student_form,}
    return render(request, "account/signup.html", context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required()
def mypage_view(request):
    username = request.user.username
    svi_moji_kolegiji = Kolegij.objects.raw('select distinct * from studij_kolegij, studij_smjer, account_moj_kolegij where studij_smjer.smjer_id = account_moj_kolegij.smjer_id and studij_kolegij.kolegij_id=account_moj_kolegij.kolegij_id and account_moj_kolegij.username= %s and studij_kolegij.studij_id=account_moj_kolegij.studij_id', [username])
    moje_objave= Objava.objects.all().filter(username=request.user).count()
    if len(list(svi_moji_kolegiji)) == 0:
        svi_moji_kolegiji = 0

    context = {'svi_moji_kolegiji' : svi_moji_kolegiji, 'moje_objave' : moje_objave}
    return render(request, "account/mypage.html", context)

def logout_view(request):
    logout(request)
    return redirect('homepage')