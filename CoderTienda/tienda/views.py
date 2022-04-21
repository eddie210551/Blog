from django.shortcuts import render

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
    

