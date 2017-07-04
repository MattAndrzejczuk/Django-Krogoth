from django.db import models
# Create your models here.



class SuperBasicModel(models.Model):
    basic_string = models.CharField(max_length=100)
    basic_bool = models.BooleanField(default=False)
    basic_int = models.IntegerField()


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')


class AngularFuseApplication(models.Model):
    # def __str__(self):
    #     return self.name
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class FuseAppComponent(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100) ### .HTML .JS .CSS     etc...
    parent_app = models.ForeignKey(AngularFuseApplication, on_delete=models.CASCADE,)
    contents = models.TextField()
    def __str__(self):
        return self.name

class FuseApplicationComponent(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100) ### .HTML .JS .CSS     etc...
    parent_app = models.ForeignKey(AngularFuseApplication, on_delete=models.CASCADE,)
    contents = models.TextField()