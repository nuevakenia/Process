"""Process URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

<<<<<<< HEAD
from Process.views import (inicio, pagina_logout,pagina_login,pagina_registro,tablero,crear_tablero,barmenu)
=======
from Process.views import (inicio, pagina_logout,pagina_login
,pagina_registro,tablero,crear_tablero,barmenu, crear_columna, 
crear_tarea, tarea_tipo, crear_documento, ModificarTablero,
custom_page_not_found, custom_server_error)
>>>>>>> fbdfabec2ca1144421b869ca89ab4a47dbccaa7c
from Process import views
from django.conf import settings
from django.templatetags.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('inicio/', views.inicio, name="inicio"),
    path('tablero/<id>/', tablero, name="tablero"),
    path('registro/', pagina_registro, name="registro"),
    path('', include('django.contrib.auth.urls')),
    path('logout/', pagina_logout, name="logout"),
    path('barmenu/', barmenu, name="barmenu"),
<<<<<<< HEAD
]
=======
    path('crear_tablero/', crear_tablero, name="crear_tablero"),
    path('tablero/', tablero, name="tablero"),
    path('crear_columna/', crear_columna, name="crear_columna"),
    path('tarea_tipo/', tarea_tipo, name="tarea_tipo"),
    path('crear_tarea/', crear_tarea, name="crear_tarea"),
    path('crear_documento/', crear_documento, name="crear_documento"),
    path('modificar_tablero/', ModificarTablero.as_view(), name="modificar_tablero"),
    path("404/", custom_page_not_found, name="custom_page_not_found"),
    path("500/", custom_server_error, name="custom_server_error"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler500 = "Process.views.custom_server_error"
>>>>>>> fbdfabec2ca1144421b869ca89ab4a47dbccaa7c
