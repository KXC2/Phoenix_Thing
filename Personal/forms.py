# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PhoenixForms(UserCreationForm):
    """
    Custom user registration form extending Django's built-in UserCreationForm.

    Adds an email field and customizes the fields used during registration.

    Attributes:
        email (EmailField): The user's email address. Required.
    """

    email = forms.EmailField(required=True)

    class Meta:
        """
        Metadata for PhoenixForms.

        Specifies the User model and fields to include in the form.
        """

        model = User
        fields = ['username', 'email', 'password1', 'password2']
