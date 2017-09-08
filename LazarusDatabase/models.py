from django.db import models
from chat.models import JawnUser


# Create your models here.
from rest_auth.models import LazarusCommanderAccount





class TotalAnnihilationMod(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    picture = models.ImageField(upload_to = 'pic_folder/')
    owner = models.ForeignKey(LazarusCommanderAccount, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name





# class TotalAnnihilationModAsset(models.Model):
#     parent = models.ForeignKey(TotalAnnihilationMod,
#                                on_delete=models.CASCADE)



class SelectedAssetUploadRepository(models.Model):
    name = models.CharField(max_length=400, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(JawnUser, related_name='author', blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)
    is_selected = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class HPIUpload(models.Model):
    lastModifiedDate = models.DateTimeField(blank=True, null=True, help_text='Last time this HPI was modified.')
    uploaded_by = models.ForeignKey(JawnUser, related_name='uploaded_by', blank=True, null=True)
    upload = models.FileField(upload_to='ta_data/', help_text='Total Annihilation HPI, UFO or CCX file.')
    date_of_upload = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text='Date & Time of upload.')
    name = models.CharField(max_length=255, blank=True, null=True, help_text='UFO/HPI file name.')
    size = models.IntegerField(blank=True, null=True, help_text='File size detected by JS uploader client.')
    type = models.CharField(max_length=10, blank=True, null=True, help_text='File extension detected by JS client.')
    TA_uploaded_file_log = models.IntegerField(blank=True, null=True,
                                               help_text='ID of TotalAnnihilationUploadedFile. -1 means file is being processed')


class LazarusModProject(models.Model):
    name = models.CharField(max_length=400, unique=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey(JawnUser, related_name='created_by', blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)
    is_selected = models.BooleanField(default=True)
    def __str__(self):
        return self.name




class LazarusModAsset(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    project_id = models.IntegerField(help_text='Faux PK, points to id of LazarusModProject.')
    uploader = models.ForeignKey(JawnUser, related_name='uploader', blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    image_thumbnail = models.CharField(max_length=120, default='/static/assets/images/logos/ARM_logo.png')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name




class LazarusModDependency(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    system_path = models.CharField(max_length=100)
    asset_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    model_schema = models.CharField(max_length=100,
                                    blank=True,
                                    null=True,
                                    help_text='Class name this asset conforms to. i.e. UnitFbiData')
    model_id = models.IntegerField(blank=True,
                                   null=True,
                                   default=-1,
                                   help_text='LazarusII Object id this dependency belongs to.')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name