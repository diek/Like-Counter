from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path(
        "login/",
        LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
]
