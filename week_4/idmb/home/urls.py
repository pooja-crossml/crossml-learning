from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name ='home' ),
    path('addmovie/', views.add_movie, name ='add_movie' ),

    
]
