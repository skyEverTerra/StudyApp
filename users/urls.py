""" students urls """

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    path(
        route="",
        view=views.StudentMainView.as_view(),
        name="StudentMainView"
    ),
    path(
        route="list/",
        view=views.TeacherListView.as_view(),
        name="TeacherListView"
    ),
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
        route="alumno/",
        view=views.SignupStudentView.as_view(),
        name="SignupAsStudent"
    ),
    path(
        route="login/",
        view=views.LoginView.as_view(),
        name="login"
    ),
    path(
        route="redirect/",
        view=views.redirection,
        name="redirect"
    ),
    path(
        route="colores/",
        view=views.game_colores,
        name="colores"
    ),
    path(
        route="logout/",
        view=views.LogoutView.as_view(),
        name="logout"
    )
]
