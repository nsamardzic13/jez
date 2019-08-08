from django.shortcuts import render

# Create your views here.

def teme_views(request):
    kolegij_id = request.session['kolegij_id']
    studij_id = request.session['studij_id']
    semestar_num = request.session['semestar_num']


    context = {'kolegij_id': kolegij_id, 'studij_id': studij_id, 'semestar_num': semestar_num}
    return render(request, 'tema/predmet.html', context)
