from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name ='home' ),
    path('addmovie/', views.add_movie, name ='addmovie' ),
    path('addartist/', views.add_artist, name ='add_artist'),
    path('addrating/', views.add_rating, name ='add_rating'),
    path('addaward/', views.add_award, name ='add_award'),
    path('topten/', views.topten, name ='topten'),
    path('leastten/', views.leastten, name ='leastten'),
    path('within/', views.within, name ='within'),
    path('search/', views.search_results, name='search_results'),

    path('av1/', views.av1, name ='av1'),

    
]
