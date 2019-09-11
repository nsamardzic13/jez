from django.urls import path
from account import urls
from . import views


from django.urls import path
from . import views

app_name = "tema"

urlpatterns = [
    path('studij=<str:studij_id>/semestar=<int:semestar_num>/smjer=<str:smjer_id>/kolegij=<str:kolegij_id>', views.teme_views, name="teme_homepage"),
]