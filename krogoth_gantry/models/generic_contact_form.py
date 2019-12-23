__version__ = '0.9.81'
__author__ = 'Matt Andrzejczuk'


from django.db import models






class GenericContactForm(models.Model):
    title = models.CharField(max_length=255)
    sender = models.CharField(max_length=120)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    was_read = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)