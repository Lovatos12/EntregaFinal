from django.contrib import admin
from django.urls import path,include

from control_foro.views import listar_foros,crear_foro,buscar_foro

urlpatterns = [
    path('foros/', listar_foros , name="lista_foro"),
    path('crear_foro/', crear_foro , name="para_crear_foro"),
    path('buscar_foro/', buscar_foro , name="para_buscar_foro"),
    
]
