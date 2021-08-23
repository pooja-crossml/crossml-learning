from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.display, name='detail'),
    path('detail/<int:id>/expense/', views.expense, name='expense'),
]
