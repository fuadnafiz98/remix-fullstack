from django.urls import path

from . import views

urlpatterns = [
    path("csrf/", views.get_csrf, name="auth-"),
    path("login/", views.login, name="auth-login"),
    path("logout/", views.logout, name="auth-logout"),
    path("session/", views.SessionView.as_view(), name="auth-session"),
    path("whoami/", views.WhoAmIView.as_view(), name="auth-whoami"),
]
