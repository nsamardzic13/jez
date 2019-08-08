from django.shortcuts import render, redirect
from tema.forms import TemaForm
from tema.models import Tema
# Create your views here.

def teme_views(request):
    kolegij_id = request.session['kolegij_id']
    studij_id = request.session['studij_id']
    semestar_num = request.session['semestar_num']
    context = {'kolegij_id': kolegij_id, 'studij_id': studij_id, 'semestar_num': semestar_num}

    if request.method == 'POST':
        form = TemaForm(data=request.POST)
        if form.is_valid():
            form.kolegij_id_id = studij_id
            form.save()
            return redirect('account:mypage')
    else:
        form = TemaForm()
        return render(request, 'tema/predmet.html', {'form':form})
