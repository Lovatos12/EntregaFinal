from django.contrib import admin
from django.urls import path

from perfiles.views import registro, login_view, CustomLogoutView,informacion_usuario,edit_profile

urlpatterns = [

    path('signup/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('profile/', informacion_usuario, name='informacion_usuario'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    
]