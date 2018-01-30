from django.db import models
import jsbeautifier
from polymorphic.models import PolymorphicModel
# Create your models here.
from krogoth_gantry.models import KrogothGantryMasterViewController






class NgIncludedHtml(PolymorphicModel):
    name = models.CharField(max_length=255, unique=True)
    contents = models.TextField(default='<h4> krogoth_gantry Error: There is nothing here yet! </h4>')
    url_helper = models.CharField(max_length=255,
                                  default='Dont worry about this text.',
                                  help_text='krogoth_gantry will take care of this.')
    def save(self, *args, **kwargs):
        self.url_helper = '/moho_extractor/NgIncludedHtml/?name=' + self.name
        super(NgIncludedHtml, self).save(*args, **kwargs)


class NgIncludedJs(PolymorphicModel):
    name = models.CharField(max_length=255, unique=True)
    contents = models.TextField(default='<h4> krogoth_gantry Error: There is nothing here yet! </h4>')
    url_helper = models.CharField(max_length=255,
                                  default='Dont worry about this text.',
                                  help_text='krogoth_gantry will take care of this.')

    def save(self, *args, **kwargs):
        self.url_helper = '/moho_extractor/NgIncludedJs/?name=' + self.name
        self.contents = jsbeautifier.beautify(self.contents)
        super(NgIncludedJs, self).save(*args, **kwargs)


class IncludedJsMaster(NgIncludedJs):
    master_vc = models.ForeignKey(KrogothGantryMasterViewController,
                                  on_delete=models.CASCADE,
                                  related_name='partial_js')


class IncludedHtmlMaster(NgIncludedHtml):
    sys_path = models.CharField(max_length=256, default='/usr/src/app/')
    master_vc = models.ForeignKey(KrogothGantryMasterViewController, on_delete=models.CASCADE,
                                  related_name='partial_html')
    def save(self, *args, **kwargs):
        saveToPath = self.master_vc.path_to_static + "partialsHTML/" + self.name
        self.sys_path = saveToPath
        super(IncludedHtmlMaster, self).save(*args, **kwargs)
