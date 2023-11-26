from django import forms
from ckeditor.fields import RichTextField

class ForoFormulario(forms.Form):
  
    nombre = forms.CharField(
        required=True,
        label="Nombre del foro",
        help_text="Ingrese el nombre del foro",
    )
    tema = forms.ChoiceField(
        choices=[("Comida", "Comida"), ("Salud", "Salud"), ("Ejercicio", "Ejercicio"), ("Otro", "Otro")],
        label="Tema del foro",
        help_text="Seleccione el tema del foro",
    )
    contenido = forms.CharField(
        required=True,
        label="Contenido del foro",
        help_text="Ingrese el contenido del foro",
    )