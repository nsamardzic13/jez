from django import forms
import re
from studij.models import Studij
from account.models import Student

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    ime = forms.CharField(max_length=30, required=True)
    prezime = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=50, required=True)
    studij_id = forms.ModelChoiceField(queryset=Studij.objects.all())
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    password_repeat = forms.CharField(max_length=30, widget=forms.PasswordInput)

    def clean_ime(self):
        ime = self.cleaned_data.get('ime')
        if not re.match("^[a-zA-Z0-9_]*$", ime):
            raise forms.ValidationError("Neispravan oblik imena!")
        return ime

    def clean_prezime(self):
        prezime = self.cleaned_data.get('prezime')

        if not re.match("^[a-zA-Z0-9_]*$", ime):
            raise forms.ValidationError("Neispravan oblik prezimena!")
        return prezime

    def clean_username(self):
        username = self.cleaned_data.get('username')
        student_flag= Student.objects.filter(username=username).exists()

        if(student_flag):
            raise forms.ValidationError("Korisničko ime se već koristi!")
        if not re.match("^[a-zA-Z0-9_]*$", username):
            raise forms.ValidationError("Neispravan oblik korisničkog imena!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        email_flag = Student.objects.filter(email=email).exists()

        if not domain == "riteh":
            raise forms.ValidationError("Potrebno je koristiti valjanu riteh mail adresu!")
        if(email_flag):
            raise forms.ValidationError("Uneseni email se već koristi!")
        return email

    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_repeat')

        if(password1 != password2):
            raise forms.ValidationError("Lozinke nisu jednake!")
        if(password1 == password2 and len(password1) < 8):
                raise forms.ValidationError("Lozinka mora imati minimalno 8 znakova!")
        return password1


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

