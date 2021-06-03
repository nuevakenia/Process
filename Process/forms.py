from django import forms
from django.forms import ModelForm
from core.models import Usuario, Tablero, Unidad , Tablero, Tarea, Tarea_columna, Columna
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.http import request


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        id_unidad = forms.ModelChoiceField(queryset=Unidad.objects.all(), required=True)
        fields = ('nombre', 'apellidop', 'apellidom', 'cargo', 'id_unidad')

class TableroForm(forms.ModelForm):
    class Meta:
        model = Tablero
        fields = ('nombre','descripcion','user')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.id = self.cleaned_data['user']

        if commit:
            user.save()
        return user

class ColumnaForm(forms.ModelForm):
    class Meta:
        model = Columna
        id_tablero = forms.ModelChoiceField(queryset=Tablero.objects.filter(user=3))
        fields = ('nombre','posicion','descripcion','id_tablero')

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fecha_creacion = forms.DateTimeField()
        fecha_termino = forms.DateTimeField()
        fields = ('nombre','descripcion','fecha_creacion','fecha_termino'
        ,'id_tipo','detalle','id_documento','user')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.id = self.cleaned_data['user']

        if commit:
            user.save()
        return user