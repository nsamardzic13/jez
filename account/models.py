from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from studij.models import Kolegij, Studij

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studij_id = models.ForeignKey(Studij, on_delete=models.CASCADE, default='psvss')
    email_ver = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_image', default='/profile_image/default.png')

    def __str__(self):
        return self.user.username

class Student_Kolegij(models.Model):
    username = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null=True)
    kolegij_id = models.ForeignKey(Kolegij, on_delete=models.DO_NOTHING, null=True)

