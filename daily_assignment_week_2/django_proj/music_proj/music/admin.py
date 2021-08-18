from django.contrib import admin
from music.models import Singer, Song, Album

admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Album)