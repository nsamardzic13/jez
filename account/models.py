from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from studij.models import Kolegij, Studij

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studij_id = models.ForeignKey(Studij, on_delete=models.CASCADE, default='pss')
    email_ver = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_image', default='/profile_image/default.png')

    def __str__(self):
        return self.user.username

class Moj_Kolegij(models.Model):
    studij_id = models.ForeignKey(Studij, on_delete=models.CASCADE, default='pss')
    username = models.CharField(max_length=150)
    kolegij_id = models.CharField(max_length=10)