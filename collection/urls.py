from django.urls import path

from .views import user_home, add_game

urlpatterns = [
    path("home", user_home, name="user_home"),
    path("add_game", add_game, name="add_game"),
]

