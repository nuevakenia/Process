from django.shortcuts import redirect, render
from .forms import ExtendedUserCreationForm, UsuarioForm, TableroForm
from core.models import Usuario, Rol, Tablero
from django.http import HttpResponse, request
from django.template import Template, Context
from django.template.loader import get_template
from django.utils import timezone
from django.db.models.functions import Concat

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.db import connection
from django.core.files.base import ContentFile
import cx_Oracle
import locale

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.aggregates import Sum

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


def tablero(request):
    tableros = Tablero.objects.all()
    data = {'tableros':tableros}
    return render(request, "tablero.html", data)

def crear_tablero(request):
    data = {
        'form':TableroForm()
    }

    if request.method == 'POST':
        formulario = TableroForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
        data['form'] = formulario

    return render(request, "crear_tablero.html", data)   

    
def barmenu(request):

    return render(request, "barmenu.html")    