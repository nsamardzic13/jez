from django import forms
from tema.models import Tema

class TemaForm(forms.ModelForm):
    tema_ime = forms.CharField(max_length=50)

    class Meta:
        model = Tema
        fields = ('tema_ime', )