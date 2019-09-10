from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
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
    form = AuthenticationForm

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
            student_form.fields['studij_id'].widget.attrs = {'class': 'form-control'}
            context = {'form': form, 'student_form': student_form}
            return render(request, "account/settings.html", context)

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

        if form.is_valid() and student_form.is_valid():
            user = form.save() #prvo spremim podatke iz forme u DJANGO USER MODEL
            student = student_form.save(commit=False) #želim spremiti u studenta al prvo pohranim podatke (commit - false) i onda nadodam podatke iz usera)
            student.user = user
            student.save()
            successful_submit = True

    else:
        successful_submit = False
        form = RegistrationForm()
        student_form = StudentProfileForm()
        student_form.fields['studij_id'].widget.attrs = {'class': 'form-control'}

    context = {'form' : form, 'student_form' : student_form, 'successful_submit': successful_submit}
    return render(request, "account/signup.html", context)



def mypage_view(request):
    #ispis sve moje kolegije
    username = request.user.username
    svi_moji_kolegiji = Kolegij.objects.raw('select * from studij_kolegij, account_moj_kolegij where studij_kolegij.kolegij_id=account_moj_kolegij.kolegij_id and account_moj_kolegij.username= %s and studij_kolegij.studij_id_id=account_moj_kolegij.studij_id_id', [username])
    moje_objave= Objava.objects.all().filter(username=request.user).count()
    if len(list(svi_moji_kolegiji)) == 0:
        svi_moji_kolegiji = 0

    context = {'svi_moji_kolegiji' : svi_moji_kolegiji, 'moje_objave' : moje_objave}
    return render(request, "account/mypage.html", context)

def logout_view(request):
    logout(request)
    return redirect('homepage')