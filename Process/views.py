from django.shortcuts import redirect, render
from .forms import ExtendedUserCreationForm, TareaTipoForm, UsuarioForm, TableroForm, ColumnaForm, TareaForm, CrearDocumentoForm, SeleccionarTableroForm, ModificarTableroForm,ListadoTableroForm
from core.models import Usuario, Unidad, Tablero, Columna, Tarea, Tarea_columna, Tarea_tipo
from django.http import HttpResponse, request
from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from django.utils import timezone
from django.db.models.functions import Concat

from django.views.generic import ListView
from django.views.generic import View
from copy import copy

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

# error 404
def custom_page_not_found(request):
    
    return render(request,'custom_page_not_found.html')

# error 500
def custom_server_error(request):
    usuario = request.user
    if request.method == 'GET' and usuario.is_authenticated:
        dataTablero = Tablero.objects.filter(user=usuario.id)
        context = { 'tableros' : dataTablero }
    return render(request,'custom_server_error.html', context)

@login_required(login_url="login")
def inicio(request):
    usuario = request.user
    if request.method == 'GET' and usuario.is_authenticated:
        usr = get_object_or_404(Usuario, user=usuario.id)
        ult_tablero = Usuario.objects.filter(user=usuario.id).values_list("ultimo_tablero", flat=True)
        return redirect('tablero', id=usr.ultimo_tablero)
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
                messages.warning(request, 'Password Incorrecta!')
                print("password incorrecta!")
                return redirect('registro')
            else:
                print("Registro exitoso")
            if formularioRegistro.is_valid and usuario_form.is_valid():
                
                user = formularioRegistro.save()
                usuario = usuario_form.save(commit=False)
                usuario.user = user
                usuario.save()
                messages.success(request, 'Usuario registrado con éxito')
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


@login_required(login_url="login")
def tablero(request,id):
    usuario = request.user
    ult_tablero = Usuario.objects.filter(user=usuario.id).values_list("ultimo_tablero", flat=True)
    dataTablero = Tablero.objects.filter(user=usuario.id)
    dataTableroEscogido = get_object_or_404(Tablero, id_tablero=id)
    dataUltTablero = Tablero.objects.filter(id_tablero=ult_tablero)
    dataColumna = Columna.objects.filter(id_tablero=id)
    dataTarea = Tarea.objects.filter(user=1)
    Usuario.objects.filter(user=usuario.id).update(ultimo_tablero=id)  
    context = {
    'tableros' : dataTablero,'formSelcTab' : SeleccionarTableroForm(instance=dataTableroEscogido),'columnas' : dataColumna, 'tareas' : dataTarea ,'crear_columnas' : ColumnaForm()
    }
    if request.method == 'GET':
        if 'crear_columna' in request.POST:
            formulario = ColumnaForm(request.POST or None)
            if formulario.is_valid():
                formulario.save()
                context['mensaje'] = "Guardado correctamente"
                context['crear_columnas']= formulario
                
    if request.method == 'POST':
        if 'crear_columna' in request.POST:
            formulario = ColumnaForm(request.POST or None)
            if formulario.is_valid():
                formulario.save()
                context['mensaje'] = "Guardado correctamente"
                context['crear_columnas']= formulario

        if 'tablero_seleccionado' in request.POST:
            form_tab_seleccionado = SeleccionarTableroForm(request.POST, instance=dataTableroEscogido)
            #Usuario.objects.filter(user=usuario.id).update(ultimo_tablero=ultimo_tablero)
            if form_tab_seleccionado.is_valid():
                form_tab_seleccionado.save()
                return redirect('tablero/',id)
            context['formSelcTab']= form_tab_seleccionado  
               # print("Exito,Nuevo tablero ID: ",dataUltTablero)              
    return render(request, "tablero.html", context)

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

def listar_tareas(request):
    tableros = Tablero.objects.all()
    data = {'tableros':tableros}
    return render(request, "xxtablero.html", data)

@login_required(login_url="login")
def crear_tablero(request):
    context ={}
    usuario = request.user
    if request.method == 'POST':
        formulario = TableroForm(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            ult_tablero = Tablero.objects.filter(user=usuario.id).values_list("id_tablero", flat=True).last()
            print("Ultimo tablero: ", ult_tablero)
            usr = get_object_or_404(Tablero, id_tablero=usuario.id)
            messages.success(request, 'Tablero creado correctamente')
          #  nuevo_tablero = formulario.cleaned_data.get('nombre')
           # print("id tablero creado ",nuevo_tablero)
            return redirect('tablero', id=ult_tablero)
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
            messages.success(request, 'Tarea Tipo submission successful')
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
        "detalle" : "",
        "detalle" : "Deta de la tarea",
        "id_documento" : 1
    }

    if request.method == 'POST':
        formulario = TareaForm(request.POST or None, initial = dict_inicial)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tablero seleccionado con éxito!')
        context['crear_tarea']= formulario

    return render(request, "crear_tarea.html", context)



def crear_documento(request):
    context = {
        'crearDocumento': CrearDocumentoForm()
    } 
    if request.method == 'POST':
        formulario = CrearDocumentoForm(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Documento creado con éxito!')
        context['crearDocumento']= formulario
    return render(request, "crear_documento.html", context)



class ModificarTablero(View):

    def get(self, request, *args, **kwargs):
        usuario = request.user
        form = ModificarTableroForm(usuario)
        

        ult_tablero = Usuario.objects.filter(user=usuario.id).values_list("ultimo_tablero", flat=True)
        update_tablero = Usuario.objects.filter(user=usuario.id).update(ultimo_tablero=ult_tablero)
        tableros = Tablero.objects.filter(id_tablero=ult_tablero[0:1].get())
        return render(request, "modificar_tablero.html", {"form": form, "tableros":tableros})

    '''
class ModificarTablero(View):

    def get(self, request, *args, **kwargs):
        usuario = request.user
        form = ModificarTableroForm(usuario)
        
        
        ult_tablero = Usuario.objects.filter(user=usuario.id).values_list("ultimo_tablero", flat=True)
        update_tablero = Usuario.objects.filter(user=usuario.id).update(ultimo_tablero=ult_tablero)
        tableros = Tablero.objects.filter(id_tablero=ult_tablero[0:1].get())
        return render(request, "modificar_tablero.html", {"form": form, "tableros":tableros})
    
    def post(self, request, *args, **kwargs):
        usuario = request.user
        form = ModificarTableroForm(usuario)
        
        ult_tablero = Usuario.objects.filter(user=usuario.id).values_list("ultimo_tablero", flat=True)
        update_tablero = Usuario.objects.filter(user=usuario.id).update(ultimo_tablero=ult_tablero)
        tableros = Tablero.objects.filter(id_tablero=ult_tablero[0:1].get())

        if form.is_valid():
            print("todo okei")
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
        return render(request, "modificar_tablero.html", {"form": form, "tableros":tableros})

    def post(self, request, *args, **kwargs):
        usuario = request.user
        context = {} 
        form = ModificarTableroForm(request.POST, instance=usuario)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
        context['crearDocumento']= form
        return render(request, "modificar_tablero.html", context)  
    
    def modificar_tablero(request, id_tablero):
    tablero = get_object_or_404(Usuario, user=id_tablero)
   # ult_tablero = Usuario.objects.filter(user=usuario.id).values_list("ultimo_tablero", flat=True)
   # dataUltTablero = Tablero.objects.filter(id_tablero=ult_tablero)
    context = {
        'ult_tablero': ModificarTableroForm(instance=tablero) 
    }
    return render(request, "modificar_tablero.html", context)


    def listado_tablero(request):
    usuario = request.user
    tableros = Tablero.objects.filter(user=usuario)
    data = {
        'tableros': SeleccionarTableroForm()
    }
     if request.method == 'POST':
        formulario = SeleccionarTableroForm(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Documento creado con éxito!')
        context['crearDocumento']= formulario
    

    contador = Carro.objects.filter(id_carro=usuario.id).count()
    data = {'tableros':tableros}
    return render(request, "tableros.html", data)

    class crear_tarea(ListView):
    context = {
        'form': TareaForm()
    }

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

    def post(self, request, *args, **kwargs):
        formulario = TareaForm(request.POST or None, initial = dict_inicial)
        if formulario.is_valid():
            formulario.save()
            print("Exitoso creacion tarea")
            messages.success(request, 'Tarea  submission successful')
            context['crear_tarea']= formulario
    template_name = 'plantillas/crear_tarea.html'




def listado_tablero(request,id_tablero):
    usuario = request.user
    ult_tablero = Usuario.objects.filter(user=usuario.id).values_list("ultimo_tablero", flat=True)
    dataTablero = Tablero.objects.filter(user=usuario.id)
    dataUltTablero = Tablero.objects.filter(id_tablero=ult_tablero)
    dataColumna = Columna.objects.filter(id_tablero=ult_tablero[0:1].get())
    dataTarea = Tarea.objects.filter(user=1)
    tableros = Tablero.objects.filter(user=usuario)
    data = {
        'tableros': dataTablero, 'ultimo_tablero':SeleccionarTableroForm(): 
    }
     if request.method == 'POST':
        formulario = SeleccionarTableroForm(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tablero seleccionado con éxito!')
        context['select_tablero']= formulario
    return render(request, "tableros.html", context, data)


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
        "detalle" : "",
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

'''