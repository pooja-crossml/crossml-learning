from django.db import models

class Awards(models.Model):
    Name = models.CharField(max_length = 20)
    Date = models.DateTimeField()


class Movie(models.Model):
    Name = models.CharField(max_length = 20)
    Genure = models.CharField(max_length = 20)
    Release_Date = models.DateTimeField()
    avg_rating = models.IntegerField()
    Language = models.CharField(max_length = 20)
    Artist = models.CharField(max_length = 20)
    Length = models.DecimalField(max_digits = 4,decimal_places=2)
    Awards = models.ManyToManyField(Awards)


class Artist(models.Model):

    GENDER_CHOICES = (("male", "male"),
    ("female", "female"),
    ("other", "other"))

    Name = models.CharField(max_length = 20)
    Date_of_Birth = models.DateTimeField()
    Gender = models.CharField(max_length=10, choices= GENDER_CHOICES,default = 'male') 
    movie = models.ManyToManyField(Movie)  
    Awards = models.ManyToManyField(Awards)




class Rating(models.Model):
    RATING_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"))
    Rating = models.CharField(max_length = 20,choices = RATING_CHOICES, default = '0')
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    Votes = models.IntegerField()




# # Rating
# # 	- Rating (0-10)
# # 	- Movie
# # 	- Votes
# # Movie
# # 	- Name
# # 	- Genre
# # 	- Release Date
# # 	- Avg Rating
# # 	- Language
# # 	- Artists
# # 	- Length
# # 	- Awards received
# # Artists
# # 	- Name
# # 	- Date of Birth
# # 	- Gender
# # 	- Awards received
# # Awards
# # 	- Name
# # 	- Date
# #          -Type (single/ Multipl)
# # Rating
# # 	- Rating (0-10)
# # 	- Movie
# # 	- Votes
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