from django import forms
import re
from objava.models import Objava

class ObjavaForm(forms.ModelForm):
    class Meta:
        model = Objava
        fields = ('tekst',)
