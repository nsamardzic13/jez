from django.db import models
from tema.models import Tema
from django.contrib.auth.models import User
from account.models import Student
from django.utils import timezone
import os


class Objava(models.Model):
    objava_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    kolegij_id = models.CharField(max_length=500, default="NN")
    tema = models.ForeignKey(Tema, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)
    tekst = models.TextField()
    likes = models.IntegerField(default=0)

    def getfiles(self):
        return Objava_Files.objects.filter(objava_id=self.objava_id)

    def getlikes(self):
        if Objava_Likes.objects.filter(objava_id_id = self.objava_id):
            self.likes = Objava_Likes.objects.filter(objava_id_id = self.objava_id).count()
        else:
            self.likes = 0
        return self.likes

    def isliked(self):
        return Objava_Likes.objects.filter(objava_id_id = self.objava_id).exists()

    def getprofileimage(self):
        return User.objects.get(username=self.username)

    def __str__(self):
        return self.objava_id

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

    def getlikes(self):
        if Objava_Likes.objects.filter(objava_id_id = self.objava.objava_id):
            self.objava.likes = Objava_Likes.objects.filter(objava_id_id = self.objava.objava_id).count()
        else:
            self.objava.likes = 0
        return self.objava.likes

    def isliked(self):
        return Objava_Likes.objects.filter(objava_id_id = self.objava.objava_id).exists()

class Objava_Likes(models.Model):
    objava_id = models.ForeignKey(Objava, on_delete=models.DO_NOTHING)
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING)

