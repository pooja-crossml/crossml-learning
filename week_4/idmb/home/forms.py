from django.forms import ModelForm
from .models import Movie, Artist

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"
