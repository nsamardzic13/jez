from django.urls import path
from . import views

app_name = "objava"

urlpatterns = [
    path('studij=<str:studij_id>/smjer=<str:smjer_id>/semestar=<int:semestar_num>/kolegij=<str:kolegij_id>/tema=<int:tema_id>', views.objava_view, name="objava_homepage"),
    path('like/', views.like_view, name = "like"),
    path('report/', views.report_view, name = "report"),
]