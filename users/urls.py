""" students urls """

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    path(
        route="select/",
        view=views.SelectionView.as_view(),
        name="select"
    ),
    path(
        route="maestro/",
        view=views.SignupTeacherView.as_view(),
        name="SignupAsTeacher"
    ),
    path(
        route="login/",
        view=views.LoginView.as_view(),
        name="login"
    ),
    path(
        route="whoami/",
        view=views.mostrar_usuario,
        name="ms"
    )
]
