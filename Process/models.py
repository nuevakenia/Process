from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
import os

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=99)
    comuna = models.CharField(max_length=99)
    provincia = models.CharField(max_length=99)
    region = models.CharField(max_length=99)
    fecha_nacimiento = models.CharField(max_length=99)
    sexo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=99)
    def __str__(self):
        return self.nombre