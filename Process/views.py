from django.shortcuts import redirect, render
from .forms import ExtendedUserCreationForm, TareaTipoForm, UsuarioForm, TableroForm, ColumnaForm, TareaForm
from core.models import Usuario, Unidad, Tablero, Columna, Tarea, Tarea_columna, Tarea_tipo
from django.http import HttpResponse, request
from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from django.utils import timezone
from django.db.models.functions import Concat

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib import messages
from django.db import connection
from django.core.files.base import ContentFile
import cx_Oracle
import locale

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.aggregates import Sum
# CACHE
# from django.views.decorators.cache import cache_page

# cache_page(200)

def inicio(request):
    
    return render(request, "inicio.html")

def pagina_logout(request):
    logout(request)
    return redirect('login')

def pagina_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.warning(request, 'Identificación Correcta!')
            return redirect('inicio')

        else:
            messages.warning(request, 'Identificación Incorrecta!')

    return render(request, 'login.html',{'titulo':'Identifícate'})

def pagina_registro(request):
        if request.method == 'POST':
            formularioRegistro = UserCreationForm(request.POST)
            usuario_form = UsuarioForm(request.POST)
            password = request.POST["password1"]
            confirmation = request.POST["password2"]
            if password != confirmation:
                messages.warning(request, 'Identificación Correcta!')
            if formularioRegistro.is_valid and usuario_form.is_valid():
                user = formularioRegistro.save()
                usuario = usuario_form.save(commit=False)
                usuario.user = user

                usuario.save()
                username = formularioRegistro.cleaned_data.get('username')
                password = formularioRegistro.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                
                return redirect('inicio')
        else:
            formularioRegistro = ExtendedUserCreationForm()
            usuario_form = UsuarioForm()

        context = {'formularioRegistro' : formularioRegistro, 'usuario_form' : usuario_form}
        return render(request, 'registro.html', context)


##
def tablero(request):
    usuario = request.user
    ult_tablero = Usuario.objects.filter(user=usuario.id).values_list("ultimo_tablero", flat=True)
    dict_crear_columna = {
        "nombre" : "Nombre Columna",
        "posicion" : "Posición Columna",
        "descripcion" : "Descripción Columna",
        "id_tablero" : 1
        }
    dataTablero = Tablero.objects.filter(user=usuario.id)
    dataUltTablero = Tablero.objects.filter(id_tablero=ult_tablero)
    dataColumna = Columna.objects.filter(id_tablero=ult_tablero[0])
    dataTarea = Tarea.objects.filter(id_tarea=1)
    context = {
    'tableros' : dataTablero,'ultimotablero' : dataUltTablero,'columnas' : dataColumna, 'tareas' : dataTarea ,'crear_columnas' : ColumnaForm()
    }
    if request.method == 'POST':
        if 'crear_columna' in request.POST:
            formulario = ColumnaForm(request.POST or None, initial = dict_crear_columna)
            if formulario.is_valid():
                formulario.save()
                context['mensaje'] = "Guardado correctamente"
                context['crear_columnas']= formulario

        if 'tablero_seleccionado' in request.POST:
            form_tab_seleccionado = SeleccionarTableroForm(request.POST or None)
            Usuario.objects.filter(user=usuario.id).update(ultimo_tablero=tab_seleccionado)
            if form_tab_seleccionado.is_valid():
                form_tab_seleccionado.save()
                context['tab_select']= form_tab_seleccionado                
    return render(request, "tablero.html", context)


def crear_columna(request):
    context = {
        'form':ColumnaForm()
    } 
    usuario = request.user
    dict_inicial = {
        "nombre" : "Nombre Columna",
        "posicion" : "Nombre Columna",
        "descripcion" : "Descripción Columna",
        "id_tablero" : 1
        }
    if request.method == 'POST':
        formulario = ColumnaForm(request.POST or None, initial = dict_inicial)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = "Guardado correctamente"
        context['form']= formulario
    return render(request, "crear_columna.html", context)

def crear_tarea(request):
    tableros = Tablero.objects.all()
    data = {'tableros':tableros}
    return render(request, "xxxxtablero.html", data)

def listar_tareas(request):
    tableros = Tablero.objects.all()
    data = {'tableros':tableros}
    return render(request, "xxtablero.html", data)

@login_required(login_url="login")
def crear_tablero(request):
    context ={}
    usuario = request.user
    dict_inicial = {
        "user" : 1,
        "nombre" : "Nombre Tablero",
        "descripcion" : "Descripción tablero"
        }
    if request.method == 'POST':
        formulario = TableroForm(request.POST or None, initial = dict_inicial)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = "Guardado correctamente"
        context['form']= formulario
    return render(request, "crear_tablero.html", context)   

def barmenu(request):

    return render(request, "barmenu.html")

def tarea_tipo(request):
    context = {
        'form': TareaTipoForm()
    } 
    usuario = request.user

    dict_inicial = {
        "nombre" : "Nombre Tarea Tipo",
        "descripcion" : "Descripción Tarea Tipo",
        "id_documento" : 1
        }

    if request.method == 'POST':
        formulario = TareaTipoForm(request.POST or None, initial = dict_inicial)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = "Guardado correctamente"
        context['tarea_tipo']= formulario
    return render(request, "tarea_tipo.html", context)


def crear_tarea(request):
    context = {
        'form': TareaForm()
    }

    usuario = request.user

    dict_inicial = {
        "nombre" : "Nombre de la tarea",    
        "descripcion" : "Descripcion de la tarea", 
        "fecha_creacion" : "Fecha de creacion de la tarea", 
        "fecha_termino" : "Fecha de termino de la tarea",
        "user" : 1,
        "id_tipo" : 1, 
        "detalle" : "Deta de la tarea",
        "id_documento" : 1
    }

    if request.method == 'POST':
        formulario = TareaForm(request.POST or None, initial = dict_inicial)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = "Guardado correctamente"
        context['crear_tarea']= formulario

    return render(request, "crear_tarea.html", context)