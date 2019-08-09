from django.shortcuts import render, redirect
from tema.forms import TemaForm
from tema.models import Tema
# Create your views here.

def teme_views(request, studij_id, kolegij_id, semestar_num):
    sve_teme = Tema.objects.all().filter(kolegij_id=kolegij_id)
    form = TemaForm()
    context = {'kolegij_id': kolegij_id, 'studij_id': studij_id, 'semestar_num': semestar_num,'sve_teme': sve_teme, 'form': form}

    if request.method == 'POST':
        form = TemaForm(data=request.POST)
        if form.is_valid():
            nova_tema = form.save(commit=False) #dodali smo temu u commjt al moramo nadodati id kolegij i provjeriti postoji li već takva tema!
            #triba provjeriti postoji li već takva tema za taj kolegij!
            nova_tema.kolegij_id = kolegij_id
            nova_tema.save()
            form = TemaForm() #opet inicijaliziram formu da mi se očisti textbox
            return render(request, 'tema/predmet.html', context)
    else:
        #kad prvi put pristupiš stranici prikaži formu i sve postojeće teme!
        return render(request, 'tema/predmet.html', context)
