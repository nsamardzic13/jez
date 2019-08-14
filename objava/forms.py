from django import forms
import re
from objava.models import Objava, Objava_Files
from django.forms import ClearableFileInput

class ObjavaForm(forms.ModelForm):
    class Meta:
        model = Objava
        fields = ('tekst',)

class FilesObjavaForm(forms.ModelForm):
    class Meta:
        model = Objava_Files
        fields = ('attachment',)
        widgets = {
            'attachment': ClearableFileInput(attrs={'multiple': True}),
        }