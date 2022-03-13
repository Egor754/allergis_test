from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class SignUpForm(UserCreationForm):
    """User registration form."""
    first_name = forms.CharField(
        max_length=30,
        required=True,
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
    )
    email = forms.EmailField(
        max_length=254,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class SignInForm(AuthenticationForm):
    """User login form."""
    class Meta:
        model = User
        fields = ("email", "password")