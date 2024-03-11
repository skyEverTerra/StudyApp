""" students urls """

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    path(
        route="select/",
        view=views.SelectLogin.as_view(),
        name="select"
    ),
    path(
        route="login/",
        view=views.LoginView.as_view(),
        name="login"
    )
]
