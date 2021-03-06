from django.db import models
from django.utils import timezone
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User
import os
import datetime
from django.forms.fields import DateTimeField
from django.core.signals import request_started, request_finished
from django.db.models.signals import post_save, pre_save

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

class Unidad(models.Model):
    id_unidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=255,null=True, blank=True)
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=99)
    fecha_creacion = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    id_columna = models.ForeignKey('Columna', on_delete=models.CASCADE)
    id_tipo = models.ForeignKey('Tarea_tipo', on_delete=models.CASCADE, null=True, blank=True)
    tarea_madre = models.ForeignKey('Tarea', on_delete=models.CASCADE, null=True, blank=True)
    detalle = models.CharField(max_length=255,blank=True, null=True)
    id_documento = models.ForeignKey('Documento', on_delete=models.CASCADE, null=True, blank=True)
    estado = models.IntegerField(blank=True, null=True)
    estado_avance = models.IntegerField(blank=True, null=True)
    posicion = models.IntegerField(blank=False, null=False)
    def __str__(self):
        return self.nombre

class Tarea_tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=99, null=True, blank=True)
    id_documento = models.ForeignKey('Documento', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombre

class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=255,null=True, blank=True)
    archivo = models.FileField(null=True, blank=True, upload_to="documentos/")
    def __str__(self):
        return self.nombre

class Tablero(models.Model):
    id_tablero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=255,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Columna(models.Model):
    id_columna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    posicion = models.IntegerField(blank=False, null=False)
    descripcion = models.CharField(max_length=255,null=True, blank=True)
    id_tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)
    final = models.BooleanField()
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    id_tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    reporte = models.BooleanField()
    def __str__(self):
        return self.asunto

class Flujo(models.Model):
    id_flujo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255,null=True, blank=True)
    def __str__(self):
        return self.nombre
    
class Flujo_detalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_flujo = models.ForeignKey(Flujo, on_delete=models.CASCADE)
    id_tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    posicion_tarea = models.IntegerField()
    id_columna = models.ForeignKey(Columna, on_delete=models.CASCADE)

'''
def print_semaforo(sender, instance, **kwargs):
    
    print("tenemos una request en TAREA")

post_save.connect(print_semaforo, sender = Tarea)

def print_started(sender, **kwargs):
    
    print("tenemoos una request de DOCUMENTO")

request_started.connect(print_started)
'''