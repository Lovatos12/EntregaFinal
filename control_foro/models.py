from django.db import models

# Create your models here.
class CrearForo(models.Model):
    temas_foros = (("Comida", "Comida"),
                    ("Salud", "Salud"),
                    ("Ejercio", "Ejercicio"),
                    ("Otro", "Otro"))

    nombre = models.CharField(max_length=64, blank=False, verbose_name="Nombre del Foro")
    tema = models.CharField(max_length=7, choices=temas_foros)

    # Definir un valor predeterminado manualmente (por ejemplo, el contenido predeterminado de un foro)
    contenido = models.CharField(max_length=1500, blank=False, verbose_name="Contenido del Foro", default='Bienvenido a este foro!')

    def __str__(self):
        return f"{self.tema} ,{self.nombre}"