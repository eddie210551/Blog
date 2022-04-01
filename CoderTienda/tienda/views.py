from django.shortcuts import render

# Create your views here.

def     Tienda(request):
    return render(request,'tienda/Tienda.html')
    
def     Main(request):
    context = {}
    return render(request,'tienda/Main.html',context)
    
def     Carro(request):
    context = {}
    return render(request,'tienda/Carro.html',context)
    
def     Pagos(request):
    context = {}
    return render(request,'tienda/Pagos.html',context)
    

