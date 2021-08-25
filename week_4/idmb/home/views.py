from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Artist, Rating, Award
from .forms import MovieForm, ArtistForm,AwardForm, RatingForm
from django.db.models import Avg


def index(req):
    return render(req, 'home/index.html')

def add_movie(req):
    form=MovieForm
    if req.method=='POST':
        form = MovieForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'home/add_movie.html', {'context':form})
    else:
        return render(req, 'home/add_movie.html', {'context':form})


def add_artist(req):
    form=ArtistForm
    if req.method == 'POST':
        form = ArtistForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'home/add.html', {'context':form})
            
            # return HttpResponse("Yeppie!!!!!")
    else:
        return render(req, 'home/add.html', {'context':form})


def add_rating(req):
    form=RatingForm
    if req.method=='POST':
        form = RatingForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'home/add.html', {'context':form})
    else:
        return render(req, 'home/add.html', {'context':form})


def add_award(req):
    form=AwardForm
    if req.method=='POST':
        form = AwardForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'home/add.html', {'context':form})
    else:
        return render(req, 'home/add.html', {'context':form})

# def index(request):
#     form=MovieForm
#     if request.method=='POST':
#         add_movie=MovieForm(request.POST)
#         if add_movie.is_valid():
#             add_movie.save()
#             return render(request,'Home/index.html',{'form':form})
#     return render(request,'Home/index.html',{'form':form})


def av1(request):
    a=Rating.objects.all().filter(movie=1).aggregate(Avg('rating'))
    print(a)

    return HttpResponse(a['rating__avg'])