from django.db import models
#from compositekey import db

# Create your models here.
class Studij(models.Model):
    studij_id = models.CharField(max_length=10, primary_key=True)
    studij_ime = models.CharField(max_length=60)

    def __str__(self):
        return self.studij_ime


class Kolegij(models.Model):
    dummy_id = models.AutoField(primary_key=True)
    kolegij_id = models.CharField(max_length=10)
    kolegij_ime = models.CharField(max_length=60)
    semestar = models.SmallIntegerField()
    studij_id = models.ForeignKey(Studij, on_delete=models.CASCADE)

    def __str__(self):
        return self.kolegij_ime
