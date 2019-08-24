from django.shortcuts import render, redirect
from .models import Studij, Kolegij
from account.models import  Moj_Kolegij

def homepage(request):
    predd = Studij.objects.all().filter(studij_ime__startswith='P')
    dipl = Studij.objects.all().filter(studij_ime__startswith='D')
    context = {
        'predd': predd,
        'dipl': dipl,
    }
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
    username = request.session['username']


    #sad ide botun za dodati kolegij u omiljeni, tj maknuti iz omiljenih! prvo treba pronaći sve
    if request.method == 'POST': #ako sam stisla neki botun
        moj_kolegij_id = request.POST['kolegij_id']
        #ako već postoji u Student_Kolegij znači da ga želi maknuti od tamo inače dodaje
        postoji = Moj_Kolegij.objects.filter(username=username, kolegij_id=moj_kolegij_id, studij_id_id=studij_id)
        if postoji:
            #brisi me
            Moj_Kolegij.objects.filter(username=username, kolegij_id=moj_kolegij_id).delete()
        else:
            #dodaj me
            moj_kolegij = Moj_Kolegij(username=username, kolegij_id=moj_kolegij_id, studij_id_id=studij_id)
            moj_kolegij.save()

    kolegiji = Kolegij.objects.all().filter(semestar=semestar_num, studij_id_id=studij_id)
    svi_moji_kolegiji = list(Moj_Kolegij.objects.all().filter(username=username, studij_id_id=studij_id).values_list('kolegij_id', flat=True))
    context={'kolegiji': kolegiji, 'studij_id': studij_id, 'semestar_num': semestar_num, 'svi_moji_kolegiji': svi_moji_kolegiji, }

    return render(request, 'studij/kolegiji.html', context)

def predmet(request, studij_id, kolegij_id, semestar_num):
    return redirect('tema:teme_homepage', studij_id=studij_id, semestar_num=semestar_num, kolegij_id=kolegij_id)

