from django.urls import path
from . import views

app_name = "kontakt"

urlpatterns = [
    path('', views.kontakt, name="kontakt"), #landing page kontakta
]