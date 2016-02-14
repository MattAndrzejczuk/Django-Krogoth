from django.db import models
from polymorphic import PolymorphicModel
from django.contrib.auth.models import User


# Create your models here.
class JawnUser(models.Model):
    base_user = models.OneToOneField(User, related_name='jawn_user', )
    profile_pic = models.ImageField(upload_to="media/", blank=True, null=True)
    about_me = models.CharField(max_length=400, blank=True, null=True)
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    SEX = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    sex = models.CharField(choices=SEX, null=True, blank=True, max_length=10)

    def __str__(self):
        return self.base_user.username


class Channel(models.Model):
    name = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(JawnUser, related_name='creator', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name


class Message(PolymorphicModel):
    date_posted = models.DateTimeField(auto_now_add=True)
    jawn_user = models.ForeignKey(JawnUser, related_name='user', blank=True, null=True)
    channel = models.ForeignKey(Channel, related_name='messages')


class ImageMessage(Message):
    CHOICES = (('image', 'image'),)
    type = models.CharField(max_length=50, default='image', choices=CHOICES)
    image_url = models.ImageField(upload_to='media/')
    caption = models.TextField(max_length=1000, blank=True, null=True)

    def as_json(self):
        return str(dict(
            date_posted = self.date_posted.isoformat(),
            jawn_user_id = self.jawn_user.id,
            channel = self.channel.name.__str__(),
            type = self.type.__str__(),
            image_url = self.image_url.url,
            caption = self.caption.__str__(),
        )).replace("'", '"')

class TextMessage(Message):
    CHOICES = (('text', 'text'),)
    type = models.CharField(max_length=50, default='text', choices=CHOICES)
    text = models.TextField(max_length=1000)

    def as_json(self):
        return str(dict(
            date_posted = self.date_posted.isoformat(),
            jawn_user_id = self.jawn_user.id,
            channel = self.channel.name.__str__(),
            type = self.type.__str__(),
            text = self.text.__str__(),
            id = self.pk
        )).replace("'", '"')

