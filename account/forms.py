from django import forms
import re
from studij.models import Studij
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from account.models import Student
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    ime = forms.CharField(max_length=30, required=True)
    prezime = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'ime', 'prezime', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")

        check_email = User.objects.all().filter(email=email)

        if check_email.exists():
            raise forms.ValidationError("Korisnik s ovim email-om već postoji!")
        if not domain == "riteh":
            raise forms.ValidationError("Potrebno je koristiti riteh mail adresu!")
        return email

    def clean_ime(self):
        ime = self.cleaned_data['ime']
        if not re.match("^[abcdčćdđefghijklmnoprstštuvzžxyz]", ime):
            raise forms.ValidationError("Neispravan oblik imena!")
        return ime

    def clean_prezime(self):
        prezime = self.cleaned_data['prezime']

        if not re.match("^[abcdčćdđefghijklmnoprstštuvzžxyz]", prezime):
            raise forms.ValidationError("Neispravan oblik prezimena!")
        return prezime


    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['ime']
        user.last_name = self.cleaned_data['prezime']

        if commit:
            user.save()
        return user

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('studij',)

class EditUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )

        widgets = {
            'email': forms.TextInput(attrs={'disabled': True},)
        }

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('studij', 'profile_image')





