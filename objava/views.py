from django.shortcuts import render, redirect
from .forms import ObjavaForm, FilesObjavaForm
from studij.models import Kolegij
from tema.models import Tema
from objava.models import Objava, Objava_Likes, Objava_Files
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def objava_view(request, studij_id, semestar_num, kolegij_id, tema_id):

    if request.method == 'POST':
        form = ObjavaForm(request.POST)
        file_form = FilesObjavaForm(request.POST, request.FILES)
        files = request.FILES.getlist('attachment')  # field name in model

        if form.is_valid() and file_form.is_valid():
            objava = form.save(commit=False)
            objava.username = request.user
            kol = Kolegij.objects.get(kolegij_id=kolegij_id, studij_id=studij_id)
            objava.kolegij_id = kol.kolegij_id
            objava.tema = Tema.objects.get(tema_id = tema_id)
            objava.save()

            for f in files:
                file_instance = Objava_Files(attachment=f, objava=objava, tema_id=tema_id)
                file_instance.save()

    sve_objave = Objava_Files.objects.all().filter(tema_id=tema_id)
    svi_lajkovi = Objava_Likes.objects.all()
    user_likes = list(Objava_Likes.objects.filter(username_id=request.user.id).values_list('objava_id', flat=True))
    context = {'form': form, 'file_form': file_form, 'sve_objave':sve_objave, 'svi_lajkovi':svi_lajkovi, 'user_likes':user_likes,}
    return render(request, 'objava/post.html', context)

def like_view(request):
    tmp_like = request.POST['html_like']
    if tmp_like == "html_like":
        Objava_Likes.objects.create(objava_id = Objava.objects.get(objava_id = request.POST['html_objava']), username = User.objects.get(username= request.POST['html_user']))
    if tmp_like == "html_dislike":
        print("aa")
        Objava_Likes.objects.filter(objava_id=Objava.objects.get(objava_id=request.POST['html_objava']), username=User.objects.get(username=request.POST['html_user'])).delete()
    return redirect('homepage')