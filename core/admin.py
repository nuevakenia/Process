from django.contrib import admin
from .models import Tarea_tipo, Unidad, Tarea, Columna, Tablero
# Register your models here.

admin.site.register(Unidad)
admin.site.register(Tarea)
admin.site.register(Columna)
admin.site.register(Tablero)