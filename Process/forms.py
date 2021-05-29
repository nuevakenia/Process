from django import forms
from django.forms import ModelForm
from core.models import Usuario, Tablero
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
        id_rol = forms.ModelChoiceField(queryset=request.user.groups.all(), required=True)
        fields = ('nombre', 'apellidop', 'apellidom', 'cargo', 'id_rol' )

class TableroForm(forms.ModelForm):
    class Meta:
        model = Tablero
        widgets = {
            'ref1': forms.HiddenInput(),
        }
        fields = ('nombre','descripcion')