from django.db import models
from studij.models import Kolegij
from tema.models import Tema
from django.contrib.auth.models import User
from account.models import Student
from django.utils import timezone
from django import forms

# Create your models here.
class Objava(models.Model):
    objava_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    kolegij_id = models.ForeignKey(Kolegij, on_delete=models.DO_NOTHING)
    tema = models.ForeignKey(Tema, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now())
    attachment = forms.FileField()
    tekst = models.TextField()

    def __str__(self):
        return self.objava_id

class Objava_Likes(models.Model):
    objava_id = models.ForeignKey(Objava, on_delete=models.DO_NOTHING)
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING)