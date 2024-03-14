""" students urls """

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    path(
        route="select/",
        view=views.Selection.as_view(),
        name="select"
    ),
    path(
        route="SignupAsTeacher/",
        view=views.SignupTeacherView.as_view(),
        name="SignupAsTeacher"
    )
]
