from django.urls import path
from account import urls
from . import views


from django.urls import path
from . import views

app_name = "tema"

urlpatterns = [
    path('teme/', views.teme_views, name="teme_views"),
]