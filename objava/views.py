from django.shortcuts import render, redirect
from .forms import ObjavaForm, FilesObjavaForm
from studij.models import Kolegij
from account.models import Student
from tema.models import Tema
from objava.models import Objava, Objava_Likes, Objava_Files, Objava_Prijava
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.


from storages.backends.s3boto3 import S3Boto3Storage, SpooledTemporaryFile







@login_required()
def objava_view(request, studij_id, semestar_num, kolegij_id, tema_id, smjer_id):
    form = ObjavaForm()
    file_form = FilesObjavaForm()
    active_student = Student.objects.get(user_id = request.user)
    tema = Tema.objects.get(tema_id=tema_id)
    tema_ime=tema.tema_ime

    if request.method == 'POST':
        form = ObjavaForm(data=request.POST)
        if form.is_valid(): #ako imam tekst ne znaci da imam i files
            objava = form.save(commit=False)
            objava.username = request.user
            kol = Kolegij.objects.get(kolegij_id=kolegij_id, studij_id=studij_id, smjer_id=smjer_id)
            objava.kolegij_id = kol.kolegij_id
            objava.tema = Tema.objects.get(tema_id = tema_id)
            objava.save()


            file_form = FilesObjavaForm(request.POST, request.FILES)
            if file_form.is_valid():
                files = request.FILES.getlist('attachment')  # field name in model
                for f in files:
                    file_instance = Objava_Files(attachment=f, objava=objava, tema_id=tema_id)
                    file_instance.save()

        #tu dodati da se prešalta na zadnju
        return HttpResponseRedirect(reverse('objava:objava_homepage', kwargs={'studij_id':studij_id, 'kolegij_id':kolegij_id, 'semestar_num':semestar_num ,'tema_id':tema_id, 'smjer_id':smjer_id}))

    sve_objave = Objava.objects.all().filter(tema_id=tema_id).order_by('objava_id')

    # ide paginacijica hehe
    paginator = Paginator(sve_objave, 4)
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


    svi_lajkovi = Objava_Likes.objects.all()
    user_likes = list(Objava_Likes.objects.filter(username_id=request.user.id).values_list('objava_id', flat=True))
    context = {
        'form': form,
        'file_form': file_form,
        'sve_objave': sve_objave,
        'svi_lajkovi': svi_lajkovi,
        'user_likes': user_likes,
        'student': active_student,
        'kolegij_id': kolegij_id,
        'page_range': page_range,
        'items': items,
        'studij_id': studij_id,
        'semestar_num': semestar_num,
        'tema_id': tema_id,
        'tema_ime': tema_ime,
        'end': max_index,
        'smjer_id':smjer_id,
        'tema_ime': tema_ime,
    }
    return render(request, 'objava/post.html', context)

@login_required()
def like_view(request):
    #print(request.POST['html_objava'])
    tmp_like = request.POST['html_like']
    active_user = User.objects.get(username= request.POST['html_user'])
    active_student = Student.objects.get(user_id=User.objects.get(username= request.POST['html_user']))
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

    studij_id = request.POST['get_studij_id']
    kolegij_id = request.POST['get_kolegij_id']
    semestar_num = request.POST['get_semestar_num']
    tema_id = request.POST['get_tema_id']
    smjer_id = request.POST['get_smjer_id']
    return HttpResponseRedirect(reverse('objava:objava_homepage', kwargs={'studij_id':studij_id, 'kolegij_id':kolegij_id, 'semestar_num':semestar_num ,'tema_id':tema_id, 'smjer_id': smjer_id}))

@login_required()
def report_view(request):
    active_user = User.objects.get(username=request.POST['html_user'])

    if not Objava_Prijava.objects.filter(objava_id = Objava.objects.get(objava_id = request.POST['html_objava']), username = active_user).exists():
        Objava_Prijava.objects.create(objava_id = Objava.objects.get(objava_id = request.POST['html_objava']), username = active_user)

    cnt = Objava_Prijava.objects.filter(username = active_user).count()
    if cnt > 15:
        active_student = Student.objects.get(user = active_user)
        active_student.email_ver = True
        active_student.save()

    studij_id = request.POST['get_studij_id']
    kolegij_id = request.POST['get_kolegij_id']
    semestar_num = request.POST['get_semestar_num']
    tema_id = request.POST['get_tema_id']
    smjer_id = request.POST['get_smjer_id']
    return HttpResponseRedirect(reverse('objava:objava_homepage',
                                        kwargs={'studij_id': studij_id, 'kolegij_id': kolegij_id,
                                                'semestar_num': semestar_num, 'tema_id': tema_id, 'smjer_id' : smjer_id}))