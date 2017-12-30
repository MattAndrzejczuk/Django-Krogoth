# coding=utf-8
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'
from django.db import models
from polymorphic.models import PolymorphicModel
from chat.models import JawnUser
from kbot_lab.abstract_models import KBNanolatheAbstractBlueprint, KBNanolatheUploadAbstract, KBNanolatheThreadAbstract




class KBNanolatheExampleUpload(KBNanolatheUploadAbstract):
    kbc_uploaded_by_user = models.ForeignKey(JawnUser, on_delete=models.CASCADE)

class KBNanolatheExamplePlain(KBNanolatheAbstractBlueprint):
    title = models.CharField(max_length=250)
    num_value = models.IntegerField()
