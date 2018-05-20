__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'

from django.db import models
from chat.models import JawnUser
from polymorphic.models import PolymorphicModel
from random import *


# Create your models here.
class AKThreadCategory(models.Model):
    uid = models.CharField(max_length=249, primary_key=True)
    title = models.CharField(max_length=248, default='new category')
    is_deleted = models.BooleanField(default=False)

    @classmethod
    def make_thread_category(cls, named: str):
        make_sample = cls(title="Sample Threads")
        make_sample.save()
        return make_sample

    def save(self, *args, **kwargs):
        count = len(AKThread.objects.all())
        p1 = self.title.replace(" ", "_").replace("?", "").replace("$", "").replace("!", "").replace("$", "")
        self.uid = p1.replace("%", "_").replace("&", "").replace("@", "").replace("^", "").replace("/", "") + str(count)
        super(AKThreadCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.uid


class AKThread(PolymorphicModel):
    uid = models.CharField(max_length=249, primary_key=True)
    title = models.CharField(max_length=257, default='new post')
    author = models.ForeignKey(JawnUser, on_delete=models.CASCADE, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    category = models.ForeignKey(AKThreadCategory, on_delete=models.CASCADE, related_name="ak_threads", null=True, blank=True)
    parent = models.ForeignKey('AKThread', on_delete=models.CASCADE, null=True, blank=True, related_name="broodling")


    def save(self, *args, **kwargs):
        count = len(AKThread.objects.all())
        p1 = self.title.replace(" ", "_").replace("?", "").replace("$", "").replace("!", "").replace("$", "")
        self.uid = p1.replace("%", "_").replace("&", "").replace("@", "").replace("^", "").replace("/", "") + str(count)
        super(AKThread, self).save(*args, **kwargs)

    def __str__(self):
        return self.uid



#class AKThreadArticle(AKThread):


# DEFAULTS:

try:
    sampleCat = AKThreadCategory.objects.filter(title="Sample Threads")
    if len(sampleCat) < 1:
        make_sample = AKThreadCategory.make_thread_category(named="Sample Threads")
        t1 = AKThread(title="First One", author=JawnUser.objects.all().first(), category=make_sample).save()
        t2 = AKThread(title="Second One", author=JawnUser.objects.all().first(), category=make_sample).save()
        t3 = AKThread(title="Reply to First One", author=JawnUser.objects.all().first(), category=make_sample,
                      parent=t1).save()
        t4 = AKThread(title="Third One", author=JawnUser.objects.all().first(), category=make_sample).save()
except:
    pass