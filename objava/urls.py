from django.urls import path
from . import views

app_name = "objava"

urlpatterns = [
    path('', views.post, name="post"),

]