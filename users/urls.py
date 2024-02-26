""" students urls """

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    path(
        route="login/",
        view=views.SelectLogin.as_view(),
        name="login"
    )
]
