
# Django
from django.db import models

# Models
from users.models import Alumno
from users.models import Materia

# Create your models here.
class Juego(models.Model):
    id_juego = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    puntos = models.IntegerField()
    tiempo_realizado = models.DateTimeField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
