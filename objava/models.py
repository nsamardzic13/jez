from django.db import models
from studij.models import Kolegij
from account.models import Student
from django.utils import timezone
from django import forms

# Create your models here.
class Objava(models.Model):
    objava_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    kolegij_id = models.ForeignKey(Kolegij, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now())
    attachment = forms.FileField()
    likes = models.IntegerField(default=0)
    allow_edit = models.BooleanField(default=False)
    tekst = models.TextField()

    def __str__(self):
        return self.objava_id

class EditObjave(models.Model):
    edit_objave_id = models.AutoField(primary_key=True)
    objava_id = models.ForeignKey(Objava, on_delete=models.DO_NOTHING, related_name="objava_id_fk")
    username = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    tekst = models.ForeignKey(Objava, on_delete=models.DO_NOTHING, related_name="tekst_id_fk")
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.edit_objave_id