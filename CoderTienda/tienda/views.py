from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from  .models import *

# Create your views here.

def     Tienda(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request,'tienda/Tienda.html',context)
    
def     Main(request):
    context = {}
    return render(request,'tienda/Main.html',context)
    
def     Carro(request):
    
    context = {}
    return render(request,'tienda/Carro.html',context)
    
def     Pagos(request):
    context = {}
    return render(request,'tienda/Pagos.html',context)


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "Tienda/Tienda.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "Tienda/Tienda.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "Tienda/Tienda.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Tienda/login.html", {"form": form})
    

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})
