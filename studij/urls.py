from django.urls import path
from account import urls
from . import views

app_name='studij'

urlpatterns = [
    path('', views.homepage, name="homepage"), #landing page studija želim da ide /account/mypage/studij/
    path('studijski_programi/studij=<str:studij_id>/smjer=<str:smjer_id>/', views.program, name="program"), #put to do studij programa
    path('studijski_programi/studij=<str:studij_id>/smjer=<str:smjer_id>/semestar=<int:semestar_num>/kolegij=<str:kolegij_id>', views.predmet, name="predmet"), #put do semestra
]