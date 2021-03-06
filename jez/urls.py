"""jez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('za_brucose/', include('za_brucose.urls')), #including urls.py from za_brucose

    path('account/', include('account.urls')), #include urls.py from account
    path('studij/', include('studij.urls')), #include urls.py from studij
    path('objava/', include('objava.urls')), #include urls.py from objava
    path('tema/', include('tema.urls')), #include urls.py from objava

    path('donacije/', include('donacije.urls')), #include urls.py from objava
    path('', views.homepage, name="homepage"), #landing page

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
