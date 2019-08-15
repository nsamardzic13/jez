from django import forms
import sys
from objava.models import Objava, Objava_Files
from django.forms import ClearableFileInput
from django.core.exceptions import ValidationError
MAX_SIZE = 524288 #5MB


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

    def clean_attachment(self):
         attachment = self.cleaned_data.get('attachment')
         sum = 0
         for a in attachment:
             sum = sum + sys.getsizeof(a) #ajmo reći da ovo odokativno dobro sumira haha
         if sum > MAX_SIZE:
             raise ValidationError("Prevelika datoteka, moguće je učitati maksimalno 5MB")
         return  attachment