from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ForumCategory(models.Model):
    title = models.CharField(max_length=100, unique=True, default='new category')
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class ForumPost(models.Model):
    title = models.CharField(max_length=100, default='new post')
    body = models.TextField(default='new post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class ForumReply(models.Model):
    body = models.TextField(default='new reply')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
