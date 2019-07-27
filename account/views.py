from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from account.forms import RegistrationForm
from account.models import Student
from django.contrib.auth.hashers import check_password

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            #ako ima nastavak u urlu redirektaj korisnika na tu stranicu, a ne na homepage
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form':form})

def account_settings(request):
    if request.user.is_authenticated:
        return render(request, 'account/settings')
    else:
        return redirect('account:login')

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            ime = request.POST.get('ime', '')
            prezime = request.POST.get('prezime', '')
            email = request.POST.get('email', '')
            password1 = request.POST.get('password', '')
            password2 = request.POST.get('password_repeat', '')
            if(password1 == password2):
                student_obj = Student(username = username, ime = ime, prezime = prezime, email = email, password = password1)
                student_obj.save()
            else:
                #neki html
                print("lala")

            return redirect('homepage')
    else:
        form = RegistrationForm()

    return render(request, 'account/signup.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('homepage')