from django import forms
from django.forms import ModelForm, fields
from core.models import Documento, Usuario, Tablero, Unidad , Tablero, Tarea, Tarea_columna, Columna, Tarea_tipo
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.http import request


class ExtendedUserCreationForm(UserCreationForm):
    class Meta:
        email = forms.EmailField(required=True)
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
   
class ListadoTableroForm(forms.ModelForm):
    class Meta:
        model = Tablero
        id_tablero = forms.ModelChoiceField(queryset=Tablero.objects.all(), required=True)
        fields = ('nombre','descripcion','user')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.id = self.cleaned_data['user']

        if commit:
            user.save()
        return user

#rellenar los fields 

class ModificarTableroForm(forms.ModelForm):
    
    def __init__(self, user, *args, **kwargs):
        super(ModificarTableroForm, self).__init__(*args, **kwargs)
        self.fields['ultimo_tablero'].queryset = User.objects.filter(pk = user.id)
    class Meta:
        model = Usuario
        ultimo_tablero = forms.ModelMultipleChoiceField(queryset=Tablero.objects.filter(user__id=21))
        widgets = {
             'user': forms.HiddenInput(),'nombre': forms.HiddenInput(), 'apellidop': forms.HiddenInput(), 'apellidom': forms.HiddenInput(), 'cargo': forms.HiddenInput(), 'id_unidad': forms.HiddenInput(),
        }
       # ultimo_tablero = forms.ModelChoiceField(queryset=Usuario.objects.all)
        fields = '__all__'

class SeleccionarTableroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        widgets = {
            'nombre': forms.HiddenInput(), 'apellidop': forms.HiddenInput(), 'apellidom': forms.HiddenInput(), 'cargo': forms.HiddenInput(), 'id_unidad': forms.HiddenInput(),
        }
        #ultimo_tablero = Usuario.ModelChoiceField(queryset=Usuario.objects.filter(ultimo_tablero=user))
        id_unidad = forms.ModelChoiceField(queryset=Unidad.objects.all(), required=True)
        fields = ('nombre', 'apellidop', 'apellidom', 'cargo', 'id_unidad', 'ultimo_tablero')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.id = self.cleaned_data['user']

        if commit:
            user.save()
        return user

class ColumnaForm(forms.ModelForm):
    class Meta:
        model = Columna
        fields = ('nombre','posicion','descripcion','id_tablero')

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('nombre','descripcion','fecha_creacion','fecha_termino','user', 'id_columna'
        ,'id_tipo','detalle','id_documento','estado','estado_avance','posicion')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.id = self.cleaned_data['user']

        if commit:
            user.save()
        return user

class TareaColumnaForm(forms.ModelForm):
    class Meta:
        model = Tarea_columna
        fecha_creacion = forms.DateTimeField()
        fecha_termino = forms.DateTimeField()
        fields = ('fecha_creacion','fecha_termino')


class TareaTipoForm(forms.ModelForm):
    class Meta:
        model = Tarea_tipo
        id_documento = forms.ModelChoiceField(queryset=Documento.objects.filter(id_documento=1))
        fields = ('nombre', 'descripcion', 'id_documento')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.id = self.cleaned_data['user']

        if commit:
            user.save()
        return user
        
class CrearDocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ('nombre', 'descripcion')