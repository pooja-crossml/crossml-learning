from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return '%s is the place' % self.name

class Restaurant(models.Model):
    serves_burger = models.BooleanField(default=False)
    serves_pizz = models.BooleanField(default = False)
    places = models.OneToOneField(Place, on_delete = models.CASCADE)

    def __str__(self):
        return "We welcome you here."


class Waiter(models.Model):
    resturant = models.ForeignKey(Restaurant, on_delete= models.CASCADE)
    name= models.CharField(max_length=20)

    def __str__(self):
        return "%s works here." % (self.name)