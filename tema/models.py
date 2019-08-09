from django.db import models
from studij.models import Kolegij

# Create your models here.
class Tema(models.Model):
    tema_id = models.AutoField(primary_key=True)
    tema_ime = models.CharField(max_length=50)
    kolegij_id = models.CharField(max_length=10)