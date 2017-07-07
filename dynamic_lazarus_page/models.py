from django.db import models
# Create your models here.
from django.contrib.auth.models import User




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


class VisitorLog(models.Model):
    date_created = models.DateTimeField(auto_created=True)
    remote_addr = models.CharField(max_length=255, blank=True, null=True)
    http_usr = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=255, blank=True, null=True)

FACTIONS = (
    ('Arm', 'Arm'),
    ('Core', 'Core'),
)
class LazarusCommanderAccount(models.Model):
    user = models.ForeignKey(User, unique=True)
    is_suspended = models.BooleanField(default=False)
    is_terminated = models.BooleanField(default=False)
    faction = models.CharField(choices=FACTIONS, max_length=25)
    profile_pic = models.CharField(max_length=255)
    about_me = models.CharField(max_length=75)


class LazarusModProject(models.Model):
    unique_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    author = models.ForeignKey(User, unique=True)