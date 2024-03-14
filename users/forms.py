"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User


class SignupForm(forms.Form):
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

    def save(self, type_user):
        """Create user and profile.
        
        args:
            type_user: type user class example Maestro
        """
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = type_user(user=user)
        profile.save()

