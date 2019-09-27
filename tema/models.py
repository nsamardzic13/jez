from django.db import models

from studij.models import Kolegij

# Create your models here.
class Tema(models.Model):
    tema_id = models.AutoField(primary_key=True)
    tema_ime = models.CharField(max_length=50)
    kolegij_id = models.CharField(max_length=10)

    def getlastpost(self):
        from objava.models import Objava
        post = Objava.objects.all().filter(tema=self.tema_id).last()
        if post is not None:
            return str(post.username) + ": " + post.tekst
        else:
            return "Budi prvi koji će nešto objaviti!"
