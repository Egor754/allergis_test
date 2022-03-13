from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View

from user.forms import SignUpForm, SignInForm

User = get_user_model()


class SignUpView(CreateView):
    """User registration view."""
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "users/auth/registration.html"


class SignInView(auth_views.LoginView):
    """User login view."""
    template_name = "users/auth/login.html"
    form_class = SignInForm


class ProfileView(LoginRequiredMixin, View):
    """User profile view."""

    def get(self, request):
        """Handle get request."""
        return render(request, "users/profile/profile.html")


logout_view = auth_views.LogoutView.as_view()

password_reset_view = auth_views.PasswordResetView.as_view(
    template_name="users/auth/password_reset.html",
)

password_reset_done_view = auth_views.PasswordResetDoneView.as_view(
    template_name="users/auth/password_reset_sent.html",
)

password_reset_confirm_view = auth_views.PasswordResetConfirmView.as_view(
    template_name="users/auth/password_reset_form.html",
)

password_reset_complete_view = auth_views.PasswordResetCompleteView.as_view(
    template_name="users/auth/password_reset_done.html",
)


def main(request):
    return render(request, "base.html")
