from os import name
from doc_manage.models import Document
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url 
from django.views.static import serve


urlpatterns = [
    path('', views.home, name= 'home'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_user, name="login"),
    path('welcome/',views.welcome_page, name="welcome"),
    path('logout/', views.user_logout, name='logout'),
    path('upload/', views.upload_file, name="upload"),
    # path('', views.report_data, name='report'),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)