from django.urls import path
from . import views

app_name = "studij"

urlpatterns = [
    #p/d preddiplomski, diplomski
    #sv/st sveučilišni, stručni
    #s studij
    #b/e/s/r bordogradnja, elektrotehnika, strojarstvo, racunarstvo
    path('psvss/', views.psvss, name="psvss"),
    path('psvsb/', views.psvsb, name="psvsb"),
    path('psvse/', views.psvse, name="psvse"),
    path('psvsr/', views.psvsr, name="psvsr"),
    path('pstss/', views.pstss, name="pstss"),
    path('pstsb/', views.pstsb, name="pstsb"),
    path('pstse/', views.pstse, name="pstse"),
    path('dsvss/', views.dsvss, name="dsvss"),
    path('dsvsb/', views.dsvsb, name="dsvsb"),
    path('dsvse/', views.dsvse, name="dsvse"),
    path('dsvsr/', views.dsvsr, name="dsvsr"),
    path('', views.homepage, name="homepage"), #landing page studija
]