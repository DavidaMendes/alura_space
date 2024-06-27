from django.urls import path
from galeria.views import index, imagem

 # Essas rotas são apenas de galeria
urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]