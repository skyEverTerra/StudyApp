""" Mixins """

# Django
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

class TeacherRequiredMixin(UserPassesTestMixin):
    """ Mixin teacher validation """
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect("users:StudentMainView")
        # return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

class StudentRequiredMixin(UserPassesTestMixin):
    """ Mixin teacher validation """
    def test_func(self):
        return not self.request.user.is_staff and not self.request.user.is_anonymous

    def handle_no_permission(self):
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
