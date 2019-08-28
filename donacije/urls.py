from django.urls import path
from . import views

app_name = "donacije"

urlpatterns = [
    path('', views.donacije, name="donacije"), #landing page kontakta
]