from django import forms
from studij.models import Studij

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    ime = forms.CharField(max_length=30, required=True)
    prezime = forms.CharField(max_length=30, required=True)
    email = forms.CharField(max_length=50, required=True)
    studij_id = forms.ModelChoiceField(queryset=Studij.objects.a)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    password_repeat = forms.CharField(max_length=30, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
