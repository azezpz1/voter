from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import AddGameForm
from .models import BoardGame


@login_required()
def user_home(request):
    return render(request, "collection/user_home.html")


@login_required()
def add_game(request):
    return render(request, "collection/add_game_form.html")

@login_required()
def add_boardgame(request):
    if request.method == "POST":
        boardgame = BoardGame()
        form = AddGameForm(instance=boardgame, data=request.POST)
        bggurl = form["bggurl"].value()
        if form.is_valid():
            form.save()
            return redirect("user_home")
    else:
        form = AddGameForm()
    form = AddGameForm()
    return render(request, "collection/add_game_form.html", {"form": form})
