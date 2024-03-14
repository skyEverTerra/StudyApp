"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Maestro(models.Model):
    """ Teacher's model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
