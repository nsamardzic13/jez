from django import forms
import re
from objava.models import Objava

class ObjavaForm(forms.ModelForm):
    tekst = forms.CharField(widget=forms.TextInput(), required=True)

    class Meta:
        model = Objava
        fields = ('tekst',)
