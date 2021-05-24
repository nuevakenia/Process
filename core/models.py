from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
import os

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=99)
    cargo = models.CharField(max_length=50)
    id_rol = models.ForeignKey('Rol', on_delete=models.CASCADE)

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=99)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)






