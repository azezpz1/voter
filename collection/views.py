from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def user_home(request):
    return render(request, "collection/user_home.html")


@login_required()
def add_game(request):
    return render(request, "collection/add_game_form.html")
