from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Studij

def homepage(request):
    smjerovi = Studij.objects.all()
    context = {'smjerovi': smjerovi}
    return render(request, 'studij/homepage.html', context)

def psvss(request):
    return render(request, 'studij/psvss.html')

def psvsb(request):
    return render(request, 'studij/psvss.html')

def psvse(request):
    return render(request, 'studij/psvss.html')

def psvsr(request):
    return render(request, 'studij/psvss.html')

def pstss(request):
    return render(request, 'studij/psvss.html')

def pstsb(request):
    return render(request, 'studij/psvss.html')

def pstse(request):
    return render(request, 'studij/psvss.html')

def dsvss(request):
    return render(request, 'studij/psvss.html')

def dsvsb(request):
    return render(request, 'studij/psvss.html')

def dsvse(request):
    return render(request, 'studij/psvss.html')

def dsvsr(request):
    return render(request, 'studij/psvss.html')