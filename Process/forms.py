from django import forms
from django.forms import ModelForm
from core.models import Usuario, Tablero
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm


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
        fields = ('nombre', 'apellidop', 'apellidom', 'cargo', 'id_rol' )

class TableroForm(forms.ModelForm):
    class Meta:
        model = Tablero
        fields = ('id_tablero','nombre','descripcion')