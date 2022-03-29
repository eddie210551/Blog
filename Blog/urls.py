
from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),  
    path( 'home/', views.homepage),
    path('profes/',views.profes),
    path('alumnos/',views.alumnos),
    path('loginalumno/',views.loginalumno),
    path('loginprofesor/', views.loginprofesor)
    #6 Para luegoview 
    # path('menu/', views.menu),
    # path('mensajes/',views.mensajes),
    

]
