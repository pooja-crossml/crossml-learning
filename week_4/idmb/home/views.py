from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Artist, Rating, Award
from .forms import MovieForm, ArtistForm


def index(req):
    return render(req, 'home/index.html')

def add_movie(req):
    if req.method=='POST':
        fm = MovieForm(req.POST)
        if fm.is_valid():
            
            return HttpResponse("Yeppie!!!!!")
    else:
        fm = MovieForm()
        return render(req, 'home/add_movie.html', {'context':fm})
