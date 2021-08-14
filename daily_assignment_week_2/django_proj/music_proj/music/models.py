from django.db import models

# model for Singer
class Singer(models.Model):
    name = models.CharField( max_length = 30)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=20)
    duration = models.DecimalField(max_digits=4, decimal_places=2)
    language = models.CharField(max_length = 20)
    singer = models.ManyToManyField(Singer)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=20)
    No_of_songs = models.IntegerField()
    language = models.CharField(max_length = 20)
    songs = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.name