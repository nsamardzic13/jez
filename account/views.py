from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Student, User

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
            active_student = Student.objects.get(user = User.objects.get(username = form.cleaned_data.get('username')))
            if user is not None:
                if user.is_active and active_student.email_ver is False:
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
    #na početku se inicijaliziraju forme, ako je poslije IF-a u slučaju nevalidne forme greške se neće ispisati
    #jer će se forma opet inicijalizirati
    form = RegistrationForm()
    student_form = StudentProfileForm()

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        student_form = StudentProfileForm(request.POST)

        if form.is_valid() and student_form.is_valid():
            user = form.save(commit = False) #prvo spremim podatke iz forme u DJANGO USER MODEL
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Aktiviraj svoj racun'
            message = render_to_string('account/acc_activate.html',
                                       {'user':user, 'domain':current_site.domain,
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                        #'uid': 'test',
                                        'token':account_activation_token.make_token(user)})
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            student = student_form.save(commit=False) #želim spremiti u studenta al prvo pohranim podatke (commit - false) i onda nadodam podatke iz usera)
            student.user = user
            student.save()
            status = 1
            context = {'status': status, }
            return render(request, "account/obavijesti.html", context)

    student_form.fields['studij'].widget.attrs = {'class': 'form-control'}
    context = {'form' : form, 'student_form' : student_form,}

    return render(request, "account/signup.html", context)

def forgotpass_view(request):
    if request.method == 'POST':
        email_html = request.POST["email_post"]
        if User.objects.filter(email = email_html).exists():
            user = User.objects.get(email = email_html)
            current_site = get_current_site(request)
            mail_subject = 'Zaboravljena lozinka'
            print(urlsafe_base64_encode(force_bytes(user.pk)))
            print(account_activation_token.make_token(user))
            message = render_to_string('account/resetpass.html',
                                       {'user': user, 'domain': current_site.domain,
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                        # 'uid': 'test',
                                        'token': account_activation_token.make_token(user)})
            to_email = email_html
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            status = 3
            context = {'status':status,}
            return render(request, "account/obavijesti.html", context)


    return render(request, "account/forgotpass.html")

def resetpass_view(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        account_activation_token.check_token(user, token)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        return HttpResponse('Link is invalid!')
    if request.method == 'POST':
        usr = request.POST["user_html"]
        password = request.POST["id_password"]
        password2 = request.POST["id_password2"]
        if password == password2 and User.objects.filter(username = usr).exists():
            usr_obj = User.objects.get(username = usr)
            usr_obj.set_password(password)
            usr_obj.save()
        return redirect("account:login")

    return render(request, "account/newpass.html", {'user':user.username, 'uidb64':uidb64, 'token':token})


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
        status = 2
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        status = 4
        #return HttpResponse('invalid link')

    context = {'status': status, }
    return render(request, "account/obavijesti.html", context)
@login_required()
def mypage_view(request):
    username = request.user.username
    svi_moji_kolegiji = Kolegij.objects.raw('select * from studij_kolegij, account_moj_kolegij where account_moj_kolegij.username=%s and studij_kolegij.studij_id=account_moj_kolegij.studij_id and studij_kolegij.smjer_id=account_moj_kolegij.smjer_id and studij_kolegij.kolegij_id=account_moj_kolegij.kolegij_id', [username])
    moje_objave= Objava.objects.all().filter(username=request.user).count()

    if len(list(svi_moji_kolegiji)) == 0:
        flag = 0
    else:
        flag = 1

    paginator = Paginator(svi_moji_kolegiji, 10)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)

    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]


    context = {'svi_moji_kolegiji' : svi_moji_kolegiji,
               'moje_objave' : moje_objave,
               'items': items,
               'page_range': page_range,
               'end': max_index,
               'flag': flag,
               }
    return render(request, "account/mypage.html", context)

def logout_view(request):
    logout(request)
    return redirect('homepage')