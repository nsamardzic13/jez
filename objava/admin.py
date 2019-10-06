from django.contrib import admin
from .models import Objava, Objava_Files, Objava_Likes, Objava_Prijava

admin.site.register(Objava)
admin.site.register(Objava_Files)
admin.site.register(Objava_Likes)
admin.site.register(Objava_Prijava)