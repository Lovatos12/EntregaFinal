# Generated by Django 4.2.6 on 2023-11-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrearForo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64, verbose_name='Nombre del Foro')),
                ('tema', models.CharField(choices=[('Comida', 'Comida'), ('Salud', 'Salud'), ('Ejercio', 'Ejercicio'), ('Otro', 'Otro')], max_length=7)),
                ('contenido', models.CharField(max_length=1500, verbose_name='Contenido del Foro')),
            ],
        ),
    ]