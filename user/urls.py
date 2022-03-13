from django.urls import path

from user.views import SignUpView, SignInView, logout_view, password_reset_view, password_reset_done_view, \
    password_reset_confirm_view, password_reset_complete_view, main

urlpatterns = [
    path("registration/", SignUpView.as_view(), name="registration"),
    path("login/", SignInView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path(
        "reset_password/",
        password_reset_view,
        name="reset_password",
    ),

    path(
        "reset_password_sent/",
        password_reset_done_view,
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        password_reset_confirm_view,
        name="password_reset_confirm",
    ),

    path(
        "reset_password_complete/",
        password_reset_complete_view,
        name="password_reset_complete",
    ),
    path("",main, name="main" )
]