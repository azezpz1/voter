from django.forms import ModelForm

from .models import BoardGame


class AddGameForm(ModelForm):
    class Meta:
        model = BoardGame
        fields = ["bggurl"]