from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
def donacije(request):
    return render(request, 'donacije/donacije.html')