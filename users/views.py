""" User's views """

# Django
from django.shortcuts import render
from django.views.generic import TemplateView

# External lib

# Create your views here.
class SelectLogin(TemplateView):
    template_name = "users/login.html"
