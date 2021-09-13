from django.urls import path,include, re_path
from rest_framework import routers

# from os import name
from . import views
router = routers.DefaultRouter()
router.register(r'DocumentViewSet', views.DocumentViewSet,basename='DocumentViewSet')

urlpatterns = [
    path('', include(router.urls)),
    path('doc-list/', views.documentList, name="doc-list"),
    path('doc-detail/<str:pk>/', views.documentDetailList, name="doc-detail"),
    path('doc-create/', views.documentCreate, name="doc-create"),
    path('find/<int:value>/', views.search, name="find"),
    # re_path('^val/(?P<title>.+)/$', SearchData.as_view()),

]

