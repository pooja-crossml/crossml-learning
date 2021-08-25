from django.db import models

class Award(models.Model):
    ''' Store award related data '''

    name = models.CharField(max_length = 20)
    date = models.DateTimeField()

    def __str__(self):
	    return self.name

class Artist(models.Model):
    ''' Store Artist data '''
    GENDER_CHOICES = (("male", "male"),
    ("female", "female"),
    ("other", "other"))

    name = models.CharField(max_length = 20)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=10, choices= GENDER_CHOICES,default = 'male')  
    award = models.ManyToManyField(Award,  blank=True)

    def __str__(self):
        return self.name



class Movie(models.Model):
    '''  store movie data   '''

    name = models.CharField(max_length = 20)
    genure = models.CharField(max_length = 20)
    release_Date = models.DateTimeField()
    avg_rating = models.DecimalField(max_digits=4, decimal_places=2)
    language = models.CharField(max_length = 20)
    artist = models.ManyToManyField(Artist)
    length = models.DecimalField(max_digits = 4,decimal_places=2)
    awards = models.ManyToManyField(Award, blank=True)

    def __str__(self):
        return f'{self.name} --->> {self.avg_rating}'
	
#  Artist = models.CharField(max_length = 20)



class Rating(models.Model):
    '''
        Store movie ratings
    '''

    RATING_CHOICES = ((1, "1"),(2, "2"),(3, "3"),(4, "4"),(5, "5"),(6, "6"),(7, "7"),(8, "8"),(9, "9"),(10, "10"),)

    rating = models.IntegerField(choices = RATING_CHOICES, default = '1')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    votes = models.IntegerField()

    def __str__(self):
        return f'{self.movie.name} --->> {self.rating}'



# # * Ability to add movie
# # 	- A movie can have multiple artists
# # * Ability to add Artists
# # * Ability to rate a movie
# # 	- Rating can be added multiple times
# # 	- Avg Rating should change automatically for movie
# # * Ability to give award to movie
# # * Ability to give award to a artist
# # Reporting
# # * Ability to view to 10 rated movies
# # * Ability to view lowest rated 10 movies
# # * Ability to view movies released between certain dates
# # * Ability to search movies by Movie Name or Artist Name (edited) 