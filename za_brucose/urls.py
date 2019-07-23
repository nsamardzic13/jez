from django.urls import path
from . import views

app_name = "za_brucose"

urlpatterns = [
    path('', views.homepage, name="homepage"), #landing page za_brucose
]