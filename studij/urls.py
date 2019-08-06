from django.urls import path
from account import urls
from . import views

app_name='studij'

urlpatterns = [
    #p/d preddiplomski, diplomski
    #sv/st sveučilišni, stručni
    #s studij
    #b/e/s/r bordogradnja, elektrotehnika, strojarstvo, racunarstvo

    path('psvsr/', views.psvsr, name="psvsr"),
    path('', views.homepage, name="homepage"), #landing page studija želim da ide /account/mypage/studij/
]