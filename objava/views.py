from django.shortcuts import render, redirect
from .forms import ObjavaForm

# Create your views here.
def post(request):
    test = request.session['test']
    if request.method == 'POST':
        form = ObjavaForm(data=request.POST)
        if form.is_valid():
            objava = form.save(commit=False)
            objava.username = request.user
            #nadodati sta sve jos treba se pokupiti
            objava.save()
            return redirect('homepage')
    else:
        form = ObjavaForm()
    return render(request, 'objava/post.html', {'form':form, 'test': test})