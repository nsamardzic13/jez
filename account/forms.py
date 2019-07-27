from django import forms
from django.db import models
from studij.models import Studij
from django.contrib.auth.forms import UserCreationForm
from account.models import Student

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    ime = forms.CharField(max_length=30, required=True)
    prezime = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=50, required=True)
    studij_id = forms.ModelChoiceField(queryset=Studij.objects.all())
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    password_repeat = forms.CharField(max_length=30, widget=forms.PasswordInput)
    """ 
    Prema ovom tutorijalu :https://www.youtube.com/watch?v=66l9b2QrBR8, ali baca error Object "super" no atribute save, nez kako to riješiti
    class Meta:
        model = Student
        fields = {'username','ime','prezime','email','password'}

    def save(self, commit=True):
        student = super(Student).save(commit=false)
        student.username= self.cleaned_data['username']
        student.ime = self.cleaned_data['ime']
        student.prezime = self.cleaned_data['prezime']
        student.email = self.cleaned_data['email']

        if commit:
            student.save()

        return student
    """


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

