from django.db import models
import jsbeautifier
from polymorphic.models import PolymorphicModel
# Create your models here.
from krogoth_gantry.models import KrogothGantryMasterViewController, KrogothGantryCategory
from django.contrib.postgres.fields import JSONField



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
    name = models.CharField(max_length=255)
    contents = models.TextField(default='/*NgIncludedJs*/')
    url_helper = models.CharField(max_length=255,
                                  default='Dont worry about this text.',
                                  help_text='krogoth_gantry will take care of this.')

    def save(self, *args, **kwargs):
        self.url_helper = '/moho_extractor/NgIncludedJs/?name=' + self.name
        if self.contents == "/*NgIncludedJs*/":
            boilerplate = "Inject this into your Master View Controller using: "
            example = "#" + self.name
            self.contents = "/* "+ boilerplate + example +" */"
        #self.contents = jsbeautifier.beautify(self.contents)
        self.contents = self.contents.replace("# ", "#")
        super(NgIncludedJs, self).save(*args, **kwargs)


## WARNING, CURRENTLY UNUSED:
# class IncludedJsMaster(NgIncludedJs):
#     master_vc = models.ForeignKey(KrogothGantryMasterViewController,
#                                   on_delete=models.CASCADE,
#                                   related_name='partial_js')


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


class IncludedJsMaster(NgIncludedJs):
    sys_path = models.CharField(max_length=256,
                                default='/usr/src/app/')
    master_vc = models.ForeignKey(KrogothGantryMasterViewController,
                                  on_delete=models.CASCADE,
                                  related_name='partial_js')

    def save(self, *args, **kwargs):
        saveToPath = self.master_vc.path_to_static + "partialsJS/" + self.name
        self.sys_path = saveToPath
        super(IncludedJsMaster, self).save(*args, **kwargs)




class GenericKGData(models.Model):
    uid = models.CharField(max_length=150, unique=True)
    category_one = models.CharField(max_length=150, default="GENERIC")
    category_two = models.CharField(max_length=150, default="GENERIC")
    date_created = models.DateTimeField(auto_now_add=True)
    header = JSONField()
    contents = JSONField()
