from django.shortcuts import redirect, render

#function for homepage request
def homepage(request):
    return render(request, 'index.html')