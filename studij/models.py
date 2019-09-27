from django.db import models
#from compositekey import db

# Create your models here.
class Studij(models.Model):
    studij_id = models.CharField(max_length=10, primary_key=True)
    studij_ime = models.CharField(max_length=60)

    def smjerovi_postoje(self):
        nema_smjerova_tag =  "!" + self.studij_id
        smjer_flag = Smjer.objects.all().filter(smjer_id=nema_smjerova_tag)

        if smjer_flag.exists():
            return False #za navedeni studij ne postoje nikakvi smjerovi jer u tablici ima !pssr npr

        return True

    def __str__(self):
        return self.studij_ime

    def getsmjerovi(self):
        return Smjer.objects.all().filter(studij_id=self.studij_id)



class Smjer(models.Model):
    smjer_id = models.CharField(max_length=10, primary_key=True)
    smjer_ime= models.CharField(max_length=60)
    studij = models.ForeignKey(Studij, on_delete=models.CASCADE, default='pss')

    def getnaziv(self):
        return self.studij.studij_ime

    def getkratica(self):
        return self.studij.studij_id

class Kolegij(models.Model):
    dummy_id = models.AutoField(primary_key=True)
    kolegij_id = models.CharField(max_length=10)
    kolegij_ime = models.CharField(max_length=60)
    semestar = models.SmallIntegerField()
    studij = models.ForeignKey(Studij, on_delete=models.CASCADE)
    smjer = models.ForeignKey(Smjer, on_delete=models.CASCADE)


    def __str__(self):
        return self.kolegij_ime
