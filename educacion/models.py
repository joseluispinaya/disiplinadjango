from django.db import models
from .validators import validar_mayor_a_cero, validar_cel
import datetime

# Create your models here. 
class Carrera(models.Model):
    nombreCarrera = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreCarrera


class TipoFalta(models.Model):
    descripcion = models.CharField(max_length=150)
    puntos = models.PositiveIntegerField(validators=[validar_mayor_a_cero,])

    def __str__(self):
        return self.descripcion

# celular = models.CharField(max_length=10, validators=[validar_cel,])
# puntos = models.PositiveIntegerField(validators=[validar_mayor_a_cero,])
class Estudiante(models.Model):
    nombres = models.CharField(max_length=50)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    apellidos = models.CharField(max_length=100)
    nroci = models.CharField(max_length=10)
    codigo = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, validators=[validar_cel,])
    correo = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombres


class Disiplina(models.Model):
    tipo_falta = models.ForeignKey(TipoFalta, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fechaAsignado=models.DateField(default=datetime.date.today)