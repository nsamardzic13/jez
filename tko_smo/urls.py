from django.urls import path
from . import views

app_name = "tko_smo"

urlpatterns = [
    path('', views.homepage, name="homepage"), #landing page tko_smo
]