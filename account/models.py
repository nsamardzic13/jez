from django.db import models
from studij.models import Kolegij, Studij

class Student(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
#    email = email + "@riteh.hr"
    studij_id = models.ForeignKey(Studij, on_delete=models.CASCADE, default='psvss')
    email_ver = models.BooleanField(default=False)

class Student_Kolegij(models.Model):
    username = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null=True)
    kolegij_id = models.ForeignKey(Kolegij, on_delete=models.DO_NOTHING, null=True)

