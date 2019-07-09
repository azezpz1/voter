from django.db import models

from django.contrib.auth.models import User


class BoardGame(models.Model):
    name = models.TextField()
    yearpublished = models.SmallIntegerField()
    minplayers = models.PositiveSmallIntegerField()
    maxplayers = models.PositiveSmallIntegerField()
    minplaytime = models.PositiveSmallIntegerField()
    maxplaytime = models.PositiveSmallIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=4)
    bggurl = models.URLField()
    bggid = models.PositiveSmallIntegerField(unique=True)


class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boardgames = models.ManyToManyField(BoardGame)
