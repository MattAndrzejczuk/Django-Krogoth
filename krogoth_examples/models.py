
# MODEL
from django.db import models



class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class TextLabel(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return self.name
class Car(models.Model):
    model_name = models.CharField(max_length=100, primary_key=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class Topping(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return self.name
class Pizza(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    toppings = models.ManyToManyField(Topping)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    def __str__(self):
        return self.room + ' ' + self.room
class Occupant(models.Model):
    full_name = models.CharField(max_length=100, primary_key=True)
    location = models.OneToOneField(Hotel, on_delete=models.CASCADE)
