""" User's views """

# Django
from django import http
from django.forms import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.templatetags.static import static

# Auth
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
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

# External
from json import dumps
from math import ceil

# Const
SUCCESS_URL = 'users:login'
RECOM = {
    "Ingles": {
        "4": "¡Excelente trabajo! Te recomendamos seguir explorando juegos mas avanzados o profundizar en otra materia con ayuda de tu maestro.",
        "3": "¡Bien hecho! Parece que te gusta la materia. Te recomendamos revisar algunos juegos clave y practicar para seguir mejorando.",
        "2": "No está mal, pero hay espacio para jugar y mejorar. Te recomendamos revisar los juegos básicos nuevamente y practicar más.",
        "1": "Todavía hay mucho por aprender. Te recomendamos revisar los juegos basicos y practicar más para fortalecer tus habilidades."
    }
} # "extracted from recom.json"

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

        # Query
        maestro = Maestro.objects.get(user=self.request.user)
        cal_alumnos = Calif.objects.all().select_related('alumno', 'materia')
        alumnos = Alumno.objects.filter(maestro=maestro).values()
        alumnos = Alumno.objects.filter(calif=None).exclude(calif=2).select_related('user')

        context['maestro'] = maestro
        context['alumnos'] = cal_alumnos
        context['alumnos_'] = alumnos
        context['recomendacion'] = RECOM

        return context

class LogoutView(LoginRequiredMixin, TemplateView):
    """ Logout current user """

    def get(self, request):
        logout(request)
        return redirect('users:login')

# Games Views
@login_required
def game_colores(request):
    """ Colores game """
    puntos = request.GET.get('puntos', '')

    try:
        alum_id = Alumno.objects.get(user=request.user.id)
        cal_alum = Calif.objects.get(alumno=alum_id).calificacion
        url_redirect = reverse('users:redirect')
        return HttpResponse(f"""Ya jugó este juego, su calificacion es: {cal_alum}, su recomendacion: {RECOM['Ingles'][f'{ceil(int(cal_alum)/25)}']} <a href="{url_redirect}">atras</a>""")
    except Calif.DoesNotExist:
        pass

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
