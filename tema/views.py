from django.shortcuts import render, redirect
from tema.forms import TemaForm
from tema.models import Tema
from account.models import Moj_Kolegij
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required()
def teme_views(request, studij_id, kolegij_id, semestar_num, smjer_id):
    username = request.user
    moj_kolegij = Moj_Kolegij.objects.filter(username=username, kolegij_id=kolegij_id).exists()

    #ispis svih postojecih tema i dodavanje novih
    sve_teme = Tema.objects.all().filter(kolegij_id=kolegij_id).order_by('-tema_id')
    form = TemaForm()

    if 'dodaj_temu' in request.POST:
        form = TemaForm(data=request.POST)
        if form.is_valid():
            nova_tema = form.save(commit=False) #dodali smo temu u commjt al moramo nadodati id kolegij i provjeriti postoji li već takva tema!
            #triba provjeriti postoji li već takva tema za taj kolegij!
            nova_tema.kolegij_id = kolegij_id
            nova_tema.save()

        context = {'kolegij_id': kolegij_id, 'studij_id': studij_id, 'semestar_num': semestar_num, 'smjer_id':smjer_id}
        return HttpResponseRedirect(reverse('tema:teme_homepage', kwargs=context))

    if 'favorit' in request.POST:
        if moj_kolegij:
            #brisi me
            Moj_Kolegij.objects.filter(username=username, kolegij_id=kolegij_id, studij_id=studij_id, smjer_id=smjer_id).delete()

        else:
            #dodaj me
            favorit = Moj_Kolegij(username=username, kolegij_id= kolegij_id, studij_id=studij_id, smjer_id=smjer_id)
            favorit.save()

        context = {'kolegij_id': kolegij_id, 'studij_id': studij_id, 'semestar_num': semestar_num, 'smjer_id':smjer_id}
        return HttpResponseRedirect(reverse('tema:teme_homepage', kwargs=context))

    paginator = Paginator(sve_teme, 10)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)

    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]


    context = {
        'kolegij_id': kolegij_id,
        'studij_id': studij_id,
        'moj_kolegij': moj_kolegij,
        'sve_teme': sve_teme,
        'form': form,
        'semestar_num': semestar_num,
        'items': items,
        'page_range': page_range,
        'end': max_index,
        'smjer_id': smjer_id
    }
    return render(request, 'tema/predmet.html', context)