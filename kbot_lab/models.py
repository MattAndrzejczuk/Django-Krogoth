# coding=utf-8
__version__ = '0.9.43'
__author__ = 'Matt Andrzejczuk'
from django.db import models
from polymorphic.models import PolymorphicModel
from krogoth_chat.models import JawnUser
from kbot_lab.abstract_models import KBNanolatheAbstractBlueprint, KBNanolatheUploadAbstract, KBNanolatheThreadAbstract




class KBNanolatheExampleUpload(KBNanolatheUploadAbstract):
    kbc_uploaded_by_user = models.ForeignKey(JawnUser, on_delete=models.CASCADE)

class KBNanolatheExamplePlain(KBNanolatheAbstractBlueprint):
    """Generates dynamic ajax forms within the krogoth_gantry.

    Should be treated as a Java/C# abstract class. KBNanolatheAbstractBlueprints are
    compiled into AngularJS code as MVCs and include user activity tracking.
    """
    title = models.CharField(max_length=250)
    num_value = models.IntegerField()
