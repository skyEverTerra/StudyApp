"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Maestro(models.Model):
    """ Teacher's model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Escuela(models.Model):
    id_escuela = models.AutoField(primary_key=True)
    nombre_escuela = models.CharField(max_length=255)

class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=255)

class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre_materia = models.CharField(max_length=255)

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nom_alumno = models.CharField(max_length=255)
    nom_padre = models.CharField(max_length=255)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

class Materia_Maestro(models.Model):
    id = models.AutoField(primary_key=True)
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
