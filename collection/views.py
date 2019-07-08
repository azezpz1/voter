from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import AddGameForm
from .models import BoardGame
from .utils import get_id_from_bggurl, get_boardgame_obj_from_bgg


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
        bggid = get_id_from_bggurl(bggurl)
        if not BoardGame.objects.filter(bggid__exact=bggid):
            # The board game hasn't been added to the database yet
            bg_obj = get_boardgame_obj_from_bgg(bggid)
            # TODO: Need to decide what we want stored in the db from the bg_obj
            if form.is_valid():
                form.save()
                return redirect("user_home")
    else:
        form = AddGameForm()
    form = AddGameForm()
    return render(request, "collection/add_game_form.html", {"form": form})
