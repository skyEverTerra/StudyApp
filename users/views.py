""" User's views """

# Django
from django import http
from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView

# Auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Mixins
from users.mixins import StudentRequiredMixin, TeacherRequiredMixin

# Urls
from django.urls import reverse, reverse_lazy

# Forms
from users.forms import SignupTeacherForm, SignupStudentForm

# Models
from users.models import Calif, Materia, Maestro, Alumno

# External lib
from typing import Any

# Const
SUCCESS_URL = 'users:login'

# Create your views here.
class SelectionView(TemplateView):
    """ Selection of type profile view
    
    ex: the teacher would select the teacher option
    """
    template_name = "users/selection.html"


class SignupTeacherView(FormView):
    """ Signup view for teacher type user """
    template_name = "users/teacherSignup.html"
    form_class = SignupTeacherForm
    success_url = reverse_lazy(SUCCESS_URL)

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class SignupStudentView(FormView):
    """ Signup view for teacher type user """
    template_name = "users/studentSignup.html"
    form_class = SignupStudentForm
    success_url = reverse_lazy(SUCCESS_URL)

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """ Login view """
    template_name = 'users/login.html'


class StudentMainView(LoginRequiredMixin, TemplateView):
    """ Main view for students """
    template_name = 'magic.html'


class TeacherListView(TeacherRequiredMixin, TemplateView):
    """ Teacher main view """
    template_name = 'teacherView.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener el maestro actual (suponiendo que está autenticado)
        maestro = Maestro.objects.get(user=self.request.user)
        
        # Obtener todos los alumnos asociados a este maestro
        alumnos = Alumno.objects.filter(maestro=maestro)#.select_related('Calif')
        
        context['alumnos'] = alumnos

        return context


# Games Views
@login_required
def game_colores(request):
    """ Colores game """
    puntos = request.GET.get('puntos', '')

    if puntos:
        print("aqui estan puntos", puntos)
        try:
            materia = Materia.objects.get(nombre_materia="Ingles").id_materia

            calif = Calif(alumno_id=request.user.alumno.id, materia_id=materia, calificacion=int(puntos))

            calif.save()

        except ValidationError:
            error_message = "Calificacion registrada"
            print(error_message)

    return render(request, 'games/Colores.html')

@login_required
def redirection(request):
    if request.user.is_staff:
        return redirect("users:TeacherListView")
    return redirect("users:StudentMainView")

@login_required
def mostrar_usuario(request):
    """ Temporal """
    usuario = request.user
    data = {
        'username': usuario.username,
        'email': usuario.email
    }
    return JsonResponse(data)
