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
            if form.is_valid():
                # The board game hasn't been added to the database yet
                bg_form = form.save(commit=False)
                # commit=False tells Django that "Don't send this to database yet.
                # I have more things I want to do with it."
                # From: https://stackoverflow.com/questions/22739701/django-save-modelform
                bg_obj = get_boardgame_obj_from_bgg(bggid)
                bg_form.name = bg_obj.name
                bg_form.yearpublished = bg_obj.yearpublished
                bg_form.minplayers = bg_obj.minplayers
                bg_form.maxplayers = bg_obj.maxplayers
                bg_form.minplaytime = bg_obj.minplaytime
                bg_form.maxplaytime = bg_obj.maxplaytime
                bg_form.weight = bg_obj.rating_average_weight
                bg_form.bggurl = bggurl
                bg_form.bggid = bggid
                bg_form.save() # Send it to the DB
                return redirect("user_home")
    else:
        form = AddGameForm()
    form = AddGameForm()
    return render(request, "collection/add_game_form.html", {"form": form})
