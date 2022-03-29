from django.db import models

# Create your models here.

class Profesor(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    materia = models.CharField(max_length=30)

    def __str__(self):
        txt = "{0} : {1} {2}"
        return txt.format(self.materia, self.nombre, self.apellido)  

class Curso(models.Model):
    curso_numero = models.PositiveBigIntegerField()
    profesor = models.CharField(max_length=30)

    def __str__(self):
        txt = "Curso: {0}"
        return txt.format(self.curso_numero)

    profesor = models.ForeignKey(Profesor, null= False, blank=False, on_delete=models.CASCADE)
    


class Alumno(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.nombre, self.apellido)
    
    curso = models.ForeignKey(Curso, null= False, blank=False, on_delete=models.CASCADE)
    

class Nota(models.Model):
    nota = models.PositiveBigIntegerField(max_length=10)
    fecha_nota = models.DateField(auto_now_add=True)
    profesor = models.ForeignKey(Profesor, null= False, blank=False, on_delete=models.CASCADE)
    materia = models.CharField(max_length=30)
    alumno = models.ForeignKey(Alumno, null= False, blank=False, on_delete=models.CASCADE)
    

    def ver_nota(self):
        txt = "{0}"
        return txt.format(self.nota)

    def __str__(self):
        txt = "{0} = {1} en {2}"
        return txt.format(self.alumno, self.nota, self.materia)
    

