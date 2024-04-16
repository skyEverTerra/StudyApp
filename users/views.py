""" User's views """


# External
import matplotlib.pyplot as plt
from json import dumps, loads
from math import ceil
from django.db.models import Avg
from io import BytesIO
import base64

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
from django.contrib.auth.models import User

# Mixins
from users.mixins import StudentRequiredMixin, TeacherRequiredMixin

# Urls
from django.urls import reverse, reverse_lazy

# Forms
from users.forms import SignupTeacherForm, SignupStudentForm, ABCform

# Models
from users.models import Calif, Materia, Maestro, Alumno

# settings
from appstudy.settings import STATIC_URL

# Const
SUCCESS_URL = 'users:login'
RECOM = loads(open(STATIC_URL + 'js/recom.json').read())

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
        alumnos = Alumno.objects.filter(maestro=maestro)

        promedios_generales = []
        for alumno in alumnos:
            promedio_alumno = Calif.objects.filter(alumno=alumno).aggregate(promedio=Avg('calificacion'))['promedio']
            if promedio_alumno is None:
                promedio_alumno = 0
            promedios_generales.append((alumno, promedio_alumno))
        cal_alumnos = promedios_generales

        # cal_alumnos = Calif.objects.filter(alumno__maestro=maestro).select_related('alumno', 'materia')
        # alumnos = Alumno.objects.filter(maestro=maestro).values()
        # alumnos = Alumno.objects.filter(maestro=maestro, calif=None).exclude(calif=2).select_related('user')
        #
        context['alumnos'] = cal_alumnos
        # context['alumnos_'] = alumnos
        context['recomendacion'] = RECOM
        context['maestro'] = maestro

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
        return HttpResponse(f"""Ya jugó este juego, su calificacion es: {cal_alum}, su recomendacion: {RECOM['Ingles'][abs(ceil(int(cal_alum)/25) - 4)]} <a href="{url_redirect}">atras</a>""")
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


class game_abc(LoginRequiredMixin, FormView):
    """ ABC game view """
    template_name = 'games/formulario_juego.html'
    form_class = ABCform

    def get(self, request, *args, **kwargs):
        nombre_materia = 'Lenguaje'

        try:
            materia = Materia.objects.get(nombre_materia=nombre_materia)
            alumno = Alumno.objects.get(user=request.user)
            cal_alum = Calif.objects.get(alumno=alumno, materia=materia).calificacion
            url_redirect = reverse('users:redirect')
            return HttpResponse(f"""Ya jugó este juego, su calificacion es: {cal_alum}, su recomendacion: {RECOM['Lenguaje'][abs(ceil(int(cal_alum)/25) - 4)]} <a href="{url_redirect}">atras</a>""")
        except (Calif.DoesNotExist, Materia.DoesNotExist):
            pass
        return render(
            request=request,
            template_name=self.template_name,
            context={}
        )
    
    def get_success_url(self):
        return reverse_lazy('users:abc')


    def form_valid(self, form):
        nombre_materia = 'Lenguaje'

        alumno = Alumno.objects.get(user=self.request.user)
        materia = Materia.objects.get(nombre_materia=nombre_materia)
        form.save(alumno, materia)
        return super().form_valid(form)


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


class GraficoCalificacionesView(TemplateView):
    template_name = 'grafico_calificaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        username = self.request.GET['a']
        user = User.objects.get(username=username)
        alumno = Alumno.objects.get(user=user)
        calificaciones = Calif.objects.filter(alumno=alumno)

        materias = [calif.materia.nombre_materia for calif in calificaciones]
        califs = [calif.calificacion for calif in calificaciones]

        plt.figure(figsize=(10, 5))
        plt.bar(materias, califs, color='skyblue')
        plt.xlabel('Materias')
        plt.ylabel('Calificaciones')
        plt.title('Calificaciones del Alumno')
        plt.xticks(rotation=0, ha='right')
        
        for i in range(len(materias)):
            plt.text(i, califs[i], f'{califs[i]:.2f}', ha='center', va='bottom')

        plt.ylim(0, 100)
        plt.tight_layout()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graph = base64.b64encode(image_png).decode()

        context['username'] = username
        context['graph'] = graph

        return context
