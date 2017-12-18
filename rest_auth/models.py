from django.db import models
from django.contrib.auth.models import User



# Anything user related will probably just go here:



FACTIONS = (
    ('ARM', 'Arm'),
    ('CORE', 'Core'),
)
class LazarusCommanderAccount(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    is_suspended = models.BooleanField(default=False)
    is_terminated = models.BooleanField(default=False)
    faction = models.CharField(choices=FACTIONS, max_length=25)
    profile_pic = models.CharField(max_length=255)
    about_me = models.CharField(max_length=75)

    def __str__(self):
        return self.user.username


