from django.shortcuts import render,redirect
from django.urls import reverse
from django.db.models import Q

from control_foro.models import CrearForo
from control_foro.forms import ForoFormulario
# Create your views here.

def listar_foros(request):
    foros=CrearForo.objects.all()
    contexto = {
        "foros": foros,
    }
    http_response = render(
        request=request,
        template_name='control_foro/foros.html',
        context=contexto,
    )
    return http_response

def crear_foro(request):
    if request.method == "POST":
        formulario = ForoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            tema= data["tema"]
            contenido=data["contenido"]
            foro = CrearForo(nombre=nombre, tema=tema, contenido=contenido)
            foro.save()
            url_exitosa = reverse("lista_foro")
            return redirect(url_exitosa)
    else:  
        formulario = ForoFormulario()
    http_response = render(
        request=request,
        template_name='control_foro/formulario_foro.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_foro(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]

        foros = CrearForo.objects.filter(
            Q(nombre__icontains=busqueda) | Q(tema__contains=busqueda)
        )

        contexto = {
            "foros": foros,
        }
        http_response = render(
            request=request,
            template_name='control_foro/foros.html',
            context=contexto,
        )

        return http_response
    
    
