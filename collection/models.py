from django.db import models

from django.contrib.auth.models import User


class BoardGame(models.Model):
    yearpublished = models.SmallIntegerField(on_delete=models.CASCADE)
    minplayers = models.PositiveSmallIntegerField(on_delete=models.CASCADE)
    maxplayers = models.PositiveSmallIntegerField(on_delete=models.CASCADE)
    minplaytime = models.PositiveSmallIntegerField(on_delete=models.CASCADE)
    maxplaytime = models.PositiveSmallIntegerField(on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=4, decimal_places=4)
    bggurl = models.URLField()
