from django.contrib import admin
from Aplicaciones.Colegio.models import Alumno, Curso, Nota, Profesor

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Nota)
admin.site.register(Curso)
admin.site.register(Profesor)
# admin.site.register(Lista_Notas)