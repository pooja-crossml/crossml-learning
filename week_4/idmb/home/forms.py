from django.forms import ModelForm
from django import forms
from .models import Movie, Artist, Rating, Award

class DateInput(forms.DateInput):
    input_type = 'date'

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            'release_Date': DateInput(),
        }
         

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"
        widgets = {
            'dob': DateInput(),
        }

class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = "__all__"
        widgets = {
            'date': DateInput(),
        }


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = "__all__"
