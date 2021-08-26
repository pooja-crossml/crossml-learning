from django import forms
import datetime
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
        breakpoint()
        form = MovieForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'home/add.html', {'context':form})
        else:
            return render(req, 'home/add.html', {'context':form})
    else:
        return render(req, 'home/add.html', {'context':form})


def add_artist(req):
    form=ArtistForm
    if req.method == 'POST':
        form = ArtistForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'home/add.html', {'context':form})
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
    

def topten(req):
    movies= Movie.objects.all().order_by('-avg_rating')[:5]
    return render(req, 'home/display.html', {"context": movies, "title":'Top 10 movies'})

def leastten(req):
    movies= Movie.objects.all().order_by('avg_rating')[:5]
    return render(req, 'home/display.html', {"context": movies, "title": 'Leaste rated 10 movies'})


def within(req):
    start_date = datetime.date(2019, 1,1)
    end_date = datetime.date(2021, 12,1)
    movies = Movie.objects.filter(release_Date__range=(start_date, end_date))
    return render(req, 'home/display.html', {"context": movies, "title": f'Search from {start_date} to {end_date}'})





def search_results(req):
    # breakpoint()
    # print(req.GET.get("q"))
    # q= req.GET.get("q")
    movies = Movie.objects.filter(name__icontains = 'Wednesday')
    artist = Artist.objects.get(name__icontains ="Kareena")
    # artist = Artist.objects.get(name=req.GET.get("q"))
    # breakpoint()
    print(artist.movie_set.all())
    movie = artist.movie_set.all()
    return render(req, 'home/search_display.html', {"context": movie})



    # def get_queryset(self): # new
    #     return City.objects.filter(
    #         Q(name__icontains='Boston') | Q(state__icontains='NY')
    #     )