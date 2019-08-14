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
    tema = models.ForeignKey(Tema, on_delete=models.DO_NOTHING, default=1)

    def gettekst(self):
        return self.objava.tekst

    def getusername(self):
        return self.objava.username

    def getdate(self):
        return self.objava.date

    # vjerovatno će se sad tu morat pozvat funkcija za getlikes od gore!


    def check_image(self):
        name, extension = os.path.splitext(str(self.attachment))
        if extension == ".jpg" or extension == ".png" or extension == ".svg":
            return True
        return False

class Objava_Likes(models.Model):
    objava_id = models.ForeignKey(Objava, on_delete=models.DO_NOTHING)
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING)

