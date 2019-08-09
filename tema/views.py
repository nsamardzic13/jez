from django.shortcuts import render, redirect
from tema.forms import TemaForm
from tema.models import Tema
from account.models import Moj_Kolegij
# Create your views here.

def teme_views(request, studij_id, kolegij_id, semestar_num):
    username = request.session['username']
    moj_kolegij = Moj_Kolegij.objects.filter(username=username, kolegij_id=kolegij_id).exists()

    #ispis svih postojecih tema i dodavanje novih
    sve_teme = Tema.objects.all().filter(kolegij_id=kolegij_id)
    form = TemaForm()
    context = {'kolegij_id': kolegij_id, 'studij_id': studij_id, 'moj_kolegij': moj_kolegij, 'sve_teme': sve_teme, 'form': form, 'semestar': semestar_num,}
    #debilana radim istu var 3 puta...

    if 'dodaj_temu' in request.POST:
        form = TemaForm(data=request.POST)
        if form.is_valid():
            nova_tema = form.save(commit=False) #dodali smo temu u commjt al moramo nadodati id kolegij i provjeriti postoji li već takva tema!
            #triba provjeriti postoji li već takva tema za taj kolegij!
            nova_tema.kolegij_id = kolegij_id
            nova_tema.save()
            form = TemaForm() #opet inicijaliziram formu da mi se očisti textbox
            context = {'kolegij_id': kolegij_id, 'studij_id': studij_id, 'moj_kolegij': moj_kolegij,
                       'sve_teme': sve_teme, 'form': form, 'semestar': semestar_num, }

            return render(request, 'tema/predmet.html', context)

    if 'favorit' in request.POST:
        if moj_kolegij:
            #brisi me
            Moj_Kolegij.objects.filter(username=username, kolegij_id=kolegij_id, studij_id_id=studij_id).delete()
            moj_kolegij = False

        else:
            #dodaj me
            favorit = Moj_Kolegij(username=username, kolegij_id= kolegij_id, studij_id_id=studij_id)
            favorit.save()
            moj_kolegij = True
        context = {'kolegij_id': kolegij_id, 'studij_id': studij_id, 'moj_kolegij': moj_kolegij, 'sve_teme': sve_teme,
                   'form': form, 'semestar': semestar_num, }
        return render(request, 'tema/predmet.html', context)

    return render(request, 'tema/predmet.html', context)