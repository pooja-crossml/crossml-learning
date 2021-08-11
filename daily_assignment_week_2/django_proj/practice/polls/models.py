from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return '%s is the place' % self.name

class Restaurant(models.Model):
    serves_burger = models.BooleanField(deafult=False)
    serves_pizz = models.BooleanField(deafult = False)
    places = models.OneToOneField(Place, on_delete = models.CASCADE. primary_key = True)

    def __str__(self):
        return "We welcome you in %s at our Resturant" % self.place.name


class Waiter(models.Model):
    resturant = models.ForeignKey(Restaurant, on_delete= models.CASCADE)
    name= models.CharField(max_length=20)

    def __str__(self):
        return "%s works at %s" (%self.name, %self.resturant)