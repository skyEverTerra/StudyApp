"""User forms."""

# Django
import random
import string
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Calif, Maestro, Alumno, Materia

class SignupTeacherForm(forms.Form):
    """Sign up form.
    Usable to register all user's type"""

    username = forms.CharField(min_length=4, max_length=36)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    ## to use later
    # first_name = forms.CharField(min_length=2, max_length=36)
    # last_name = forms.CharField(min_length=2, max_length=36)

    email = forms.EmailField(
        min_length=6,
        max_length=99,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El nombre de usuario esta en uso')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile.
        
        args:
            type_user: type user class example Maestro
        """
        data = self.cleaned_data
        data.pop('password_confirmation')
        
        chars = string.ascii_letters + string.digits
        teacher_code = ''.join(random.choice(chars) for _ in range(10))

        user = User.objects.create_superuser(**data)
        profile = Maestro(user=user, codigo_maestro=teacher_code)
        profile.save()


class SignupStudentForm(forms.Form):
    """Sign up form.
    Usable to register all user's type"""

    username = forms.CharField(min_length=4, max_length=36)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    ## to use later
    # first_name = forms.CharField(min_length=2, max_length=36)
    # last_name = forms.CharField(min_length=2, max_length=36)

    email = forms.EmailField(
        min_length=6,
        max_length=99,
        widget=forms.EmailInput()
    )

    teacher_code = forms.CharField(
        max_length=12
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('El nombre de usuario esta en uso')

        return username

    def clean(self):
        """Verify password confirmation match
        And must have a valid teacher code."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        teacher_code = data['teacher_code']
        valid_tc = Maestro.objects.filter(codigo_maestro=teacher_code)

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        if not valid_tc:
            raise forms.ValidationError('Ingrese un codigo de maestro valido')

        return data

    def save(self):
        """Create user and profile.
        
        args:
            type_user: type user class example Maestro
        """
        data = self.cleaned_data
        data.pop('password_confirmation')

        teacher_code = data['teacher_code']
        maestro = Maestro.objects.get(codigo_maestro=teacher_code)
        data.pop('teacher_code')
        
        user = User.objects.create_user(**data)
        profile = Alumno(user=user, maestro=maestro)
        profile.save()


class ABCform(forms.Form):
    """ game form """
    calif = forms.IntegerField()

    def save(self, alumno, materia):
        """ Create new calification """
        data = self.cleaned_data

        calif = data['calif']
        print(calif)
        calif = Calif(alumno=alumno, materia=materia, calificacion=calif)
        calif.save()
