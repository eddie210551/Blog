from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    asistencia = models.CharField(max_length=10)
    curso = models.PositiveBigIntegerField()
    nota = models.PositiveBigIntegerField()