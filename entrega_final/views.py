from django.shortcuts import render


# Create your views here.
def inicio_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
    )
    return http_response
