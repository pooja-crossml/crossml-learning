from django.urls import path
from . import views

urlpatterns=[
    path('', views.display, name = 'polls_display'),
    path('<int:place_id>/', views.place, name='place'),
    path('resturant', views.resturant, name='resturant'),
    path('resturant/waiter', views.waiter, name='waiter'),
]