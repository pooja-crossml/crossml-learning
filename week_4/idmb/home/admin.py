from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Movie)
admin.site.register(Artist)
admin.site.register(Rating)
admin.site.register(Awards)