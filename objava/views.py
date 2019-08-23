from django.shortcuts import render, redirect
from .forms import ObjavaForm, FilesObjavaForm
from studij.models import Kolegij
from account.models import Student
from tema.models import Tema
from objava.models import Objava, Objava_Likes, Objava_Files
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import  HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def objava_view(request, studij_id, semestar_num, kolegij_id, tema_id):
    form = ObjavaForm()
    file_form = FilesObjavaForm()
    active_student = Student.objects.get(user_id = request.user)

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

            return HttpResponseRedirect(reverse('objava:objava_homepage', kwargs={'studij_id':studij_id, 'kolegij_id':kolegij_id, 'semestar_num':semestar_num ,'tema_id':tema_id}))
    sve_objave = Objava_Files.objects.all().filter(tema_id=tema_id).order_by('objava_id')
    svi_lajkovi = Objava_Likes.objects.all()
    user_likes = list(Objava_Likes.objects.filter(username_id=request.user.id).values_list('objava_id', flat=True))
    context = {'form': form, 'file_form': file_form, 'sve_objave':sve_objave, 'svi_lajkovi':svi_lajkovi, 'user_likes':user_likes, 'student':active_student}
    return render(request, 'objava/post.html', context)

def like_view(request):
    tmp_like = request.POST['html_like']
    active_user = User.objects.get(username= request.POST['html_user'])
    active_student = Student.objects.get(user_id=User.objects.get(username= request.POST['html_objava_user']))
    if tmp_like == "html_like":
        Objava_Likes.objects.create(objava_id = Objava.objects.get(objava_id = request.POST['html_objava']), username = active_user)
    if tmp_like == "html_dislike":
        Objava_Likes.objects.filter(objava_id=Objava.objects.get(objava_id=request.POST['html_objava']), username= active_user).delete()

    likes_cnt = Objava_Likes.objects.filter(username = active_user).count()
    if likes_cnt > 30:
        if likes_cnt > 70:
            if likes_cnt > 100:
                if likes_cnt > 150:
                    active_student.stars = 5
                active_student.stars = 4
            active_student.stars = 3
        active_student.stars = 2
    else:
        active_student.stars = 1

    active_student.save()
    return redirect('homepage')