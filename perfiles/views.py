from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate


from perfiles.forms import UserRegisterForm

def registro(request):
    if request.method == "POST":

        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  
            url_exitosa = reverse('home')
            return redirect(url_exitosa)
    else:

        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='perfiles/registro.html',
        context={'form': formulario},
    )


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)

            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('home')
                return redirect(url_exitosa)
    else: 
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='perfiles/login.html',
        context={'form': form},
    )


class CustomLogoutView(LogoutView):
    template_name = 'perfiles/logout.html'
    
    
    
def informacion_usuario(request):
    # Obtener el usuario actual
    user = request.user

    context = {
        "user": user,
    }
    return render(request, "perfiles/informacion_usuario.html", context)


def edit_profile(request):
  user = request.user
  if request.method == 'POST':
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    url_exitosa = reverse('informacion_usuario')
    return redirect(url_exitosa)
  else:
    return render(request, 'perfiles/edit_profile.html', {'user': user})

    