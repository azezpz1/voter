from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import user_home, add_game

urlpatterns = [
    path("home", user_home, name="user_home"),
    path("add_game", add_game, name="add_game"),
    path(
        "login",
        LoginView.as_view(template_name="collection/login_form.html"),
        name="user_login",
    ),
    path("logout", LogoutView.as_view(), name="user_logout"),
]

