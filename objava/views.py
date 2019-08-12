from django.shortcuts import render, redirect
from .forms import ObjavaForm
from studij.models import Kolegij
from tema.models import Tema
from objava.models import Objava, Objava_Likes
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect

# Create your views here.
def objava_view(request, studij_id, semestar_num, kolegij_id, tema_id):
    sve_objave = Objava.objects.all().filter(kolegij_id = kolegij_id, tema_id = tema_id).order_by('date')
    svi_lajkovi = Objava_Likes.objects.all()

    if request.method == 'POST':
        form = ObjavaForm(request.POST, request.FILES)
        if form.is_valid():
            objava = form.save(commit=False)
            objava.username = request.user
            kol = Kolegij.objects.get(kolegij_id=kolegij_id, studij_id=studij_id)
            objava.kolegij_id = kol.kolegij_id
            objava.tema = Tema.objects.get(tema_id = tema_id)
            objava.save()
            form = ObjavaForm()
            #return redirect('objava:objava_homepage')

    else:
        form = ObjavaForm()

    return render(request, 'objava/post.html', {'form': form, 'sve_objave':sve_objave, 'svi_lajkovi':svi_lajkovi})

def like_view(request):
    Objava_Likes.objects.create(objava_id = Objava.objects.get(objava_id = request.POST['html_objava']), username = User.objects.get(username= request.POST['html_user']))
    return redirect('homepage')