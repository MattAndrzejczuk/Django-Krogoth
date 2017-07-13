from django.db import models
from django.contrib.auth.models import User



# Anything user related will probably just go here:



FACTIONS = (
    ('ARM', 'Arm'),
    ('CORE', 'Core'),
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