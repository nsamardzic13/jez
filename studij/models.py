from django.db import models

# Create your models here.
class kolegij(models.Model):
    kolegij_id = models.CharField(max_length=10, primary_key=True)
    kolegij_ime = models.CharField(max_length=40)

    def __str__(self):
        return self.kolegij_ime

class semestar(models.Model):
    semestar_br = models.PositiveSmallIntegerField()