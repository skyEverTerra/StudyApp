""" User's views """

# Django
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

# External lib

# Create your views here.
class SelectLogin(TemplateView):
    """ Selection of type profile view
    
    ex: the teacher would select the teacher option to manage
    their students
    """
    template_name = "users/login.html"

class LoginView(auth_views.LoginView):
    """ Login view for all users """
    template_name = "users/teacherLogin.html"
