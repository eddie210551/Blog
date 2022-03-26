
from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),  
    path( 'home/', views.homepage),
    path('menu/', views.menu),
    path('mensajes/',views.mensajes),
    path('musica-ingles/',views.ingles),
    path('espa/',views.espa), 
    path('ing90/',views.nov_ing)


]
