from django.apps import AppConfig
from django.core.signals import request_started
from datetime import datetime


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    

        
   # def ready(self):
        #request_started.connect(log_request)
    #def llamar_semaforo(self):
        #request_started.connect(actualizar_semaforo)

