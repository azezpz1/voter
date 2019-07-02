from django.urls import path

from .views import user_home

urlpatterns = [path("home", user_home, name="user_home")]

