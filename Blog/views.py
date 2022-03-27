from urllib import request
from django.http import HttpResponse
from django.shortcuts import render





def homepage(request):
    #return HttpResponse('homepage')
    return render(request,"homepage.html")

def profes(request):
    return render(request,"espacioprofesores.html")


def about(request):
    #return HttpResponse('about')
    return render(request,"about.html")

# Para luego

def menu(request):
    return HttpResponse('menu')

def mensajes(request):
    return HttpResponse('menajes')


