from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from account.models import Student

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
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('homepage')