from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ServiceFormulario(forms.Form):
    service = forms.CharField(max_length=50)
    chasis = forms.IntegerField()


class MecanicosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=40)

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    help_texts={k:"" for k in fields} 

class UserEditForm(UserCreationForm):
  email = forms.EmailField(required=True)
  password1 = forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']
    help_texts={k:"" for k in fields}