from django.shortcuts import render, redirect
from .forms import ObjavaForm, FilesObjavaForm
from studij.models import Kolegij
from tema.models import Tema
from objava.models import Objava, Objava_Likes, Objava_Files
from django.contrib.auth.models import User


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
                file_instance = Objava_Files(attachment=f, objava=objava)
                file_instance.save()

    sve_objave = Objava.objects.raw('select * from objava_objava, objava_objava_files where objava_objava.objava_id = objava_objava_files.objava_id and objava_objava.tema_id=%s order by objava_objava.date',[tema_id])
    svi_lajkovi = Objava_Likes.objects.all()
    form = ObjavaForm()
    file_form = FilesObjavaForm()

    context = {'form': form, 'file_form': file_form, 'sve_objave':sve_objave, 'svi_lajkovi':svi_lajkovi}
    return render(request, 'objava/post.html', context)

def like_view(request):
    Objava_Likes.objects.create(objava_id = Objava.objects.get(objava_id = request.POST['html_objava']), username = User.objects.get(username= request.POST['html_user']))
    return redirect('homepage')