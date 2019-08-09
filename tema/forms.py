from django import forms
from tema.models import Tema

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ('tema_ime',)
