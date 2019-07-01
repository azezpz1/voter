from django.db import models

from django.contrib.auth.models import User


class BoardGame(models.Model):
    yearpublished = models.SmallIntegerField()
    minplayers = models.PositiveSmallIntegerField()
    maxplayers = models.PositiveSmallIntegerField()
    minplaytime = models.PositiveSmallIntegerField()
    maxplaytime = models.PositiveSmallIntegerField()
    weight = models.DecimalField(max_digits=4, decimal_places=4)
    bggurl = models.URLField()


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boardgames = models.ManyToManyField(BoardGame)
