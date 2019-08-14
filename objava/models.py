from django.db import models
from studij.models import Kolegij
from tema.models import Tema
from django.contrib.auth.models import User
from account.models import Student
from django.utils import timezone
from django import forms
import os
# Create your models here.
class Objava(models.Model):
    objava_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    kolegij_id = models.CharField(max_length=500, default="NN")
    tema = models.ForeignKey(Tema, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)
    tekst = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.objava_id

    def get_likes(self):
        if Objava_Likes.objects.filter(objava_id_id = self.objava_id):
            self.likes = Objava_Likes.objects.filter(objava_id_id = self.objava_id).count
        else:
            self.likes = 0
        return self.likes



class Objava_Files(models.Model):
    attachment = models.FileField(upload_to='objava_att/', null=True, blank=True, max_length=500)
    objava = models.ForeignKey(Objava, on_delete=models.CASCADE)

    def extension(self):
        name, extension = os.path.splitext(str(self.attachment))
        return extension

class Objava_Likes(models.Model):
    objava_id = models.ForeignKey(Objava, on_delete=models.DO_NOTHING)
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING)

