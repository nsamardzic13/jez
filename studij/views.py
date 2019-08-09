from django.shortcuts import render, redirect
from .models import Studij, Kolegij


def homepage(request):
    smjerovi = Studij.objects.all()
    context = {'smjerovi': smjerovi}
    return render(request, 'studij/homepage.html', context)

def studijski_programi(request, studij_id):
    studij = Studij.objects.get(studij_id=studij_id)
    studij_ime = studij.studij_id
    razina = studij_id[0]
    if razina == 'p':
        razina = 0
    elif razina == 'd':
        #ode postaje zanimljivo ako je diplomski onda se prvo preusmjeravamo na biranje smjerova! pa tek onda na biranje semestara!
        razina = 1
    else:
        razina = 2 #nije nista od navedenog doslo je do zajeba

    context={'studij_id': studij_id, 'studij_ime': studij_ime, 'razina': razina}
    return render(request, 'studij/semestri.html', context)

def semestri(request, studij_id, semestar_num):
    #sad dohvaćam sve predmete koje su u prvom semestru tog studij_ida
    #braco mila
    kolegiji = Kolegij.objects.all().filter(semestar=semestar_num, studij_id_id=studij_id)
    context={'kolegiji': kolegiji, 'studij_id': studij_id, 'semestar_num': semestar_num}
    return render(request, 'studij/kolegiji.html', context)

def predmet(request, studij_id, kolegij_id, semestar_num):
    return redirect('tema:teme_homepage', studij_id=studij_id, semestar_num=semestar_num, kolegij_id=kolegij_id)

