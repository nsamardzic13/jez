from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from studij.models import Kolegij, Studij, Smjer
from objava.models import Objava
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_ver = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_image', default='/profile_image/default.png')
    stars = models.SmallIntegerField(default=1)
    studij = models.ForeignKey(Studij, on_delete=models.CASCADE)
    def getobjavanum(self):
        return str(Objava.objects.filter(username=self.user.username).count())
    def __str__(self):
        return self.user.username

class Moj_Kolegij(models.Model):
    studij = models.ForeignKey(Studij, on_delete=models.CASCADE, default='pss')
    smjer = models.ForeignKey(Smjer, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    kolegij_id = models.CharField(max_length=10)