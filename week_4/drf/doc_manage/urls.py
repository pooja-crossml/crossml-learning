from django.urls import path
from . import views


urlpatterns = [
     path('doc-list/', views.documentList, name="doc-list"),
    path('doc-detail/<str:pk>/', views.documentDetailList, name="doc-detail"),
    path('doc-create/', views.documentCreate, name="doc-create"),

]