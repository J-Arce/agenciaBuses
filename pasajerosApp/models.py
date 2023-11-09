from django.db import models

# Create your models here.

class Pasajero(models.Model):
    TIPOS_PASAJERO = [
        ('Estudiante', 'Estudiante'),
        ('AdultoMayor', 'Adulto Mayor'),
        ('Frecuente', 'Frecuente'),
        ('Normal', 'Normal'),
    ]

    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    tipoPasajero = models.CharField(max_length=20, choices=TIPOS_PASAJERO)