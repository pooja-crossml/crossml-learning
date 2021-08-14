from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'music_index'),
    path('<int:question_id>/', views.question, name = 'question'),
    path('<int:question_id>/votes', views.votes, name = 'votes'),
    path('<int:question_id>/result', views.result, name = 'result'),
]