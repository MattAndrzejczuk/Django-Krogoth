from django.db import models
import jsbeautifier
from polymorphic.models import PolymorphicModel
# Create your models here.
from krogoth_gantry.models import KrogothGantryMasterViewController, KrogothGantryCategory


class NgIncludedHtml(PolymorphicModel):
    name = models.CharField(max_length=255,
                            unique=True)
    contents = models.TextField(default='<h4> krogoth_gantry Error: There is nothing here yet! </h4>')
    url_helper = models.CharField(max_length=255,
                                  default='Dont worry about this text.',
                                  help_text='krogoth_gantry will take care of this.')

    def save(self, *args, **kwargs):
        self.url_helper = '/moho_extractor/NgIncludedHtml/?name=' + self.name
        super(NgIncludedHtml, self).save(*args, **kwargs)


class NgIncludedJs(PolymorphicModel):
    name = models.CharField(max_length=255,
                            unique=True)
    contents = models.TextField(default='<h4> krogoth_gantry Error: There is nothing here yet! </h4>')
    url_helper = models.CharField(max_length=255,
                                  default='Dont worry about this text.',
                                  help_text='krogoth_gantry will take care of this.')

    def save(self, *args, **kwargs):
        self.url_helper = '/moho_extractor/NgIncludedJs/?name=' + self.name
        self.contents = jsbeautifier.beautify(self.contents)
        super(NgIncludedJs, self).save(*args, **kwargs)


## WARNING, CURRENTLY UNUSED:
class IncludedJsMaster(NgIncludedJs):
    master_vc = models.ForeignKey(KrogothGantryMasterViewController,
                                  on_delete=models.CASCADE,
                                  related_name='partial_js')


class IncludedHtmlCoreTemplate(NgIncludedHtml):
    file_name = models.CharField(max_length=256,
                                 default='/usr/src/app/')
    os_path = models.CharField(max_length=256,
                               default='/usr/src/app/')
    meta_kind_0 = models.CharField(max_length=160,
                                   default='Layout')
    meta_kind_1 = models.CharField(max_length=160,
                                   default='Horizontal')
    meta_kind_2 = models.CharField(max_length=160,
                                   default='n/a')


class IncludedHtmlMaster(NgIncludedHtml):
    sys_path = models.CharField(max_length=256,
                                default='/usr/src/app/')
    master_vc = models.ForeignKey(KrogothGantryMasterViewController,
                                  on_delete=models.CASCADE,
                                  related_name='partial_html')

    def save(self, *args, **kwargs):
        saveToPath = self.master_vc.path_to_static + "partialsHTML/" + self.name
        self.sys_path = saveToPath
        super(IncludedHtmlMaster, self).save(*args, **kwargs)

# class ReadyForFileSystemFrontend(models.Model):
#     """Anything saved from the Web IDE needs to be recorded.
#
#     Helps speed up backupdvc a bit and more importantly, reminds you
#     save the Database copy permanently to the filesystem.
#     """
# modified_time = models.DateTimeField(auto_now_add=True)
# absolute_path = models.CharField(primary_key=True,
#                                  max_length=279,
#                                  default="/usr/src/app/")
# title = models.CharField(max_length=279)
# name = models.CharField(max_length=279)
# is_unsaved = models.BooleanField(default=True)
