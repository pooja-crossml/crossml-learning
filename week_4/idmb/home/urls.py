from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name ='home' ),
    path('addmovie/', views.add_movie, name ='addmovie' ),
    path('addartist/', views.add_artist, name ='add_artist'),
    path('addrating/', views.add_rating, name ='add_rating'),
    path('addaward/', views.add_award, name ='add_award'),
    path('av1/', views.av1, name ='av1'),

    
]
