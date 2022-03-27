from urllib import request
from django.http import HttpResponse
from django.shortcuts import render





def homepage(request):
    #return HttpResponse('homepage')
    return render(request,"homepage.html")


def about(request):
    #return HttpResponse('about')
    return render(request,"about.html")


def menu(request):
    return HttpResponse('menu')

def mensajes(request):
    return HttpResponse('menajes')

def ingles(request):
    #return HttpResponse('ingles')
    return render(request,"music_ing.html")
def espa(request):
    #return HttpResponse('espa')
    return render(request,"espa.html")


def nov_ing(request):
    return render(request,"ing90.html")

def dos_ing(request):
    return render(request,"ing00.html")

def profes(request):
    return render(request,"espacioprofesores.html")
