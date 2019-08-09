from django.shortcuts import render, redirect
from django.contrib.auth.models import  User
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from account.forms import RegistrationForm, LoginForm, StudentProfileForm
from django.contrib import messages
from .models import Student, Moj_Kolegij
from .models import Kolegij
# Create your views here.
def login_view(request):
    if request.method== 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                messages.info(request, f"hey {username}")
                return redirect('account:mypage')
            else:
                messages.error(request, "Ne valja nesto!")
        else:
                messages.error(request, "AA")
    form = AuthenticationForm()
    return render(request, "account/login.html", {'form':form})

def settings_view(request):
    if request.user.is_authenticated:
        return render(request, 'account/settings.html')
    else:
        return redirect('account:login')

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        student_form = StudentProfileForm(request.POST)

        if form.is_valid() and student_form.is_valid():
            user = form.save() #prvo spremim podatke iz forme u DJANGO USER MODEL
            student = student_form.save(commit=False) #želim spremiti u studenta al prvo pohranim podatke (commit - false) i onda nadodam podatke iz usera)
            student.user = user
            student.save()
            messages.success(request, "Bravo!")
            return redirect('homepage')

    else:
        form = RegistrationForm()
        student_form = StudentProfileForm()

    context = {'form' : form, 'student_form' : student_form}
    return render(request, "account/signup.html", context)



def mypage_view(request):
    #ispis sve moje kolegije
    username = request.session['username']
    svi_moji_kolegiji = Kolegij.objects.raw('select * from studij_kolegij, account_moj_kolegij where studij_kolegij.kolegij_id=account_moj_kolegij.kolegij_id and account_moj_kolegij.username= %s and studij_kolegij.studij_id_id=account_moj_kolegij.studij_id_id', [username])
    for k in svi_moji_kolegiji:
        print(k)
    context = {'svi_moji_kolegiji' : svi_moji_kolegiji}
    return render(request, "account/mypage.html", context)

def logout_view(request):
    logout(request)
    return redirect('homepage')