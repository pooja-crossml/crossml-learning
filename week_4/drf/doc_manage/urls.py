from django.urls import path,include
from rest_framework import routers
# from os import name
from . import views
router = routers.DefaultRouter()
router.register(r'DocumentViewSet', views.DocumentViewSet,basename='DocumentViewSet')

urlpatterns = [
    path('', include(router.urls)),
    # # path('//doc-list/', views.documentList, name="doc-list"),
    # path('doc-detail/<str:pk>/', views.documentDetailList, name="doc-detail"),
    # path('doc-create/', views.documentCreate, name="doc-create"),

]

