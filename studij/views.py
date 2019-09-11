from django.shortcuts import render, redirect
from .models import Studij, Kolegij, Smjer
from account.models import  Moj_Kolegij
from django.contrib.auth.decorators import login_required

@login_required()
def homepage(request):
    predd = Studij.objects.all().filter(studij_ime__startswith='P')
    dipl = Studij.objects.all().filter(studij_ime__startswith='D')

    context = {
        'predd': predd,
        'dipl': dipl,
    }
    return render(request, 'studij/homepage.html', context)


@login_required()
def program(request, studij_id, smjer_id):
    smjer = Smjer.objects.get(studij_id=studij_id, smjer_id=smjer_id)
    smjer_ime = smjer.smjer_ime
    kolegiji = Kolegij.objects.all().filter(studij_id=studij_id, smjer_id=smjer_id)

    context={
        'smjer': smjer,
        'smjer_ime': smjer_ime,
        'kolegiji' : kolegiji,
    }
    return render(request, 'studij/semestri.html', context)


@login_required()
def predmet(request, studij_id, kolegij_id, semestar_num, smjer_id):
    return redirect('tema:teme_homepage', studij_id=studij_id, smjer_id = smjer_id, semestar_num=semestar_num, kolegij_id=kolegij_id)

