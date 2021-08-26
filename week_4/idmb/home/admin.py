from django.contrib import admin
from .models import *
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "release_Date","language")


admin.site.register(Movie,MovieAdmin)

# admin.site.register(Movie)
admin.site.register(Artist)
admin.site.register(Rating)
admin.site.register(Award)