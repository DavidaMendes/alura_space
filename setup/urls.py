from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Essas rotas são gerais
    path('', include('galeria.urls')),
    ]
