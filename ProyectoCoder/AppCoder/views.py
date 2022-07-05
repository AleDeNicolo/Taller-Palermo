from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Service, Mecanicos, Cliente
from django.template import loader
from AppCoder.forms import ServiceFormulario, MecanicosFormulario, UserRegistrationForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_control



# Create your views here.


def mecanicos (request):
    return render(request, "AppCoder/mecanicos.html")
    

def service (request):
    return render(request, "AppCoder/service.html")
   

def cliente (request):
    return render(request, "AppCoder/cliente.html")
    

def entregables (request):
    return render(request, "AppCoder/entregables.html")
    

def inicio(self):
    plantilla = loader.get_template("AppCoder/inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def serviceFormulario(request):
    if request.method == "POST":
        miFormulario = ServiceFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion["service"]
        chasis = informacion["chasis"]
        service = Service(nombre=nombre, chasis=chasis)
        service.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ServiceFormulario()
    return render (request, "AppCoder/serviceFormulario.html", {"miFormulario":miFormulario})

def mecanicosFormulario(request):
    if request.method == "POST":
        miFormulario = MecanicosFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion["nombre"]
        apellido = informacion["apellido"]
        email = informacion["email"]
        especialidad = informacion["especialidad"]
        mecanicos = Mecanicos(nombre=nombre, apellido=apellido, email=email, especialidad=especialidad)
        mecanicos.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = MecanicosFormulario()
    return render (request, "AppCoder/mecanicosFormulario.html", {"miFormulario":miFormulario})

def busquedaChasis(request):
    return render(request, "AppCoder/busquedaChasis.html")

def buscar(request):

    if request.GET['chasis']:
        chasis = request.GET['chasis']
        service = Service.objects.filter(chasis=chasis)
        return render (request, 'AppCoder/resultadosBusqueda.html', {'service':service, 'chasis':chasis} )
    else:
        respuesta = "No se ha ingresado un dato Valido"
    return HttpResponse(respuesta)


def login_request(request):
  if request.method == "POST":
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      usuario = form.cleaned_data.get('username')
      clave = form.cleaned_data.get('password')

      user = authenticate(username=usuario, password=clave)
      if user is not None:
        login(request,user)
        return render(request, 'AppCoder/inicio.html', {'mensaje': f'Bienvenido {usuario}'})
      else:
        return render(request, 'AppCoder/inicio.html', {'mensaje': 'Datos incorrectos'})
    else:
      return render(request, 'AppCoder/inicio.html', {'mensaje': 'Error, Formulario invalido'})
  else:
    form = AuthenticationForm()
    return render(request, 'AppCoder/login.html', {'form':form})



def register_request(request):
  if request.method =="POST":
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      username =form.cleaned_data['username']
      form.save()
      return render(request, 'AppCoder/inicio.html', {'mensaje': f'Usuario{username} creado'})
    else:
      return render(request, 'AppCoder/inicio.html', {'mensaje': 'Error, no se pudo crear'})
  else:
    form = UserRegistrationForm()
    return render(request, 'AppCoder/register.html', {'form':form})

@login_required
def editarPerfil(request):
  # Viene del modelo de Django para usuarios
  usuario = request.user

  if request.method == 'POST':
    formulario = UserEditForm(request.POST, instance=usuario)
    if formulario.is_valid():
      informacion = formulario.cleaned_data
      usuario.email = informacion['email']
      usuario.password1 = informacion['password1']
      usuario.password2 = informacion['password2']
      usuario.save()
      return render(request, 'AppCoder/inicio.html', {'mensaje': 'Datos cambiado exitosamente'})
  else:
    formulario = UserEditForm(instance=usuario)
  return render(request, 'AppCoder/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})

class ClientesList(LoginRequiredMixin, ListView):
  model = Cliente
  template_name = 'AppCoder/cliente.html'

class ClienteDetalle(DetailView):
  model = Cliente
  template_name = 'AppCoder/clientesDetalle.html'

class ClienteCreacion(CreateView):
  model = Cliente
  success_url = reverse_lazy('cliente_list')
  fields = ['nombre', 'apellido', 'email']

class ClienteEdicion(UpdateView):
  model = Cliente
  success_url = reverse_lazy('cliente_list')
  fields = ['nombre', 'apellido', 'email']

class ClienteEliminacion(DeleteView):
  model = Cliente
  success_url = reverse_lazy('cliente_list')

def About(self):
    plantilla = loader.get_template("AppCoder/about.html")
    documento = plantilla.render()
    return HttpResponse(documento)

@cache_control (max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def page_not_found_view(request, exception):
  return render(request, '404.html', status=404)
