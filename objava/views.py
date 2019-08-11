from django.shortcuts import render, redirect
from .forms import ObjavaForm
from studij.models import Kolegij
from tema.models import Tema
from objava.models import Objava, Objava_Likes

# Create your views here.
def objava_view(request, studij_id, semestar_num, kolegij_id, tema_id):
    # test = request.session['test']
    username = request.session['username']
    kol = Kolegij.objects.get(kolegij_id = kolegij_id)
    sve_objave = Objava.objects.all().filter(kolegij_id = kol, tema_id = tema_id).order_by('date')
    svi_lajkovi = Objava_Likes.objects.all()

    if request.method == 'POST':
        form = ObjavaForm(data=request.POST)
        if form.is_valid():
            objava = form.save(commit=False)
            objava.username = request.user
            objava.kolegij_id = Kolegij.objects.get(kolegij_id = kolegij_id)
            objava.tema = Tema.objects.get(tema_id = tema_id)
            # nadodati sta sve jos treba se pokupiti
            objava.save()
    else:
        form = ObjavaForm()
    return render(request, 'objava/post.html', {'form': form, 'sve_objave':sve_objave, 'svi_lajkovi':svi_lajkovi})