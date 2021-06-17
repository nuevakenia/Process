from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
import os
import datetime

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=99)
    apellidop = models.CharField(max_length=99,null=True)
    apellidom = models.CharField(max_length=99,null=True)
    cargo = models.CharField(max_length=50,null=True)
    ultimo_tablero = models.IntegerField(null=True)
    id_unidad = models.ForeignKey('Unidad', on_delete=models.CASCADE)
    def __str__(self):
            return self.nombre

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=255)
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)

class Tarea(models.Model):
    id_tarea = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=99)
    descripcion = models.CharField(max_length=99)
    fecha_creacion = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fecha_termino = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_columna = models.ForeignKey('Columna', on_delete=models.CASCADE)
    id_tipo = models.ForeignKey('Tarea_tipo', on_delete=models.CASCADE)
    detalle = models.CharField(max_length=255)
    id_documento = models.ForeignKey('Documento', on_delete=models.CASCADE)
    estado = models.IntegerField(blank=True, null=True)
    estado_avance = models.IntegerField(blank=True, null=True)
    posicion = models.IntegerField(blank=False, null=False)


class Tarea_tipo(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=99)
    id_documento = models.ForeignKey('Documento', on_delete=models.CASCADE)

class Documento(models.Model):
    id_documento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=255)

class Tablero(models.Model):
    id_tablero = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=255)
    def __str__(self):
            return self.nombre

class Columna(models.Model):
    id_columna = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=255)
    id_tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)

class Tarea_columna(models.Model):
    id_tarea_columna = models.IntegerField(primary_key=True)
    id_tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    id_columna = models.ForeignKey(Columna, on_delete=models.CASCADE)
    fecha_creacion = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fecha_termino = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    

class Comentario(models.Model):
    id_comentario = models.IntegerField(primary_key=True)
    asunto = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    id_tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    reporte = models.BooleanField()


