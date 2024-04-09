"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models

# Models

# Create your models here.
class Maestro(models.Model):
    """ Teacher model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codigo_maestro = models.CharField(max_length=12, null=True)

class Materia(models.Model):
    """ Materia model """
    id_materia = models.AutoField(primary_key=True)
    nombre_materia = models.CharField(max_length=255)

class Alumno(models.Model):
    """ Student model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_alumno = models.CharField(max_length=255)
    nom_padre = models.CharField(max_length=255)
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE, null=True)

class Calif(models.Model):
    """ Califications models """
    id_calif = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True)
    calificacion = models.FloatField() # 1 - 10 or 10 - 100

    class Meta:
        # Enforce unique constraint on alumno and materia fields together
        unique_together = ['alumno', 'materia']
