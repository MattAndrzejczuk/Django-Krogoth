from django.db import models
from chat.models import JawnUser
import codecs

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
    is_deleted = models.BooleanField(default=False)
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
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    system_path = models.CharField(max_length=250)
    raw_string_url = models.TextField(blank=True,
                                      null=True,
                                      help_text='URL to display raw file as a string.',
                                      default='nan')
    asset_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    model_schema = models.CharField(max_length=250,
                                    blank=True,
                                    null=True,
                                    help_text='Class name this asset conforms to. i.e. UnitFbiData')
    model_id = models.IntegerField(blank=True,
                                   null=True,
                                   default=-1,
                                   help_text='LazarusII Object id this dependency belongs to.')
    meta_data = models.TextField(blank=True,
                                null=True,
                                help_text='Useful for showing info on HTML frontend.',
                                default='nan')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        remove_syspath = self.system_path.replace('/usr/src/persistent/media/ta_data/','')
        urlencoded = remove_syspath.replace('/', '_SLSH_')
        self.raw_string_url = '/LazarusDatabase/rawDependencyAsTextView?syspath=' + urlencoded
        super(LazarusModDependency, self).save(*args, **kwargs)


class LazarusPublicAsset(models.Model):
    user_uploader = models.ForeignKey(JawnUser, related_name='user_uploader', blank=True, null=True)
    likes = models.IntegerField(help_text='Users who liked this asset.', default=0)
    dislikes = models.IntegerField(help_text='Users that disliked this asset.', default=0)
    side = models.CharField(max_length=100, help_text='Arm or Core faction', default='ARM')
    name = models.CharField(max_length=100, help_text='name of this unit', default='No Name')
    encoded_path = models.CharField(max_length=125, help_text='The sys path to the FBI file with Url encoding', default='NOTAIR')

    tags = models.CharField(max_length=125, help_text='i.e. VTOL TANK LEVEL2 KBOT NOTAIR', default='NOTAIR')
    description = models.TextField(blank=True,
                                 null=True,
                                 help_text='Summary info about this unit asset.',
                                 default='nan')

    unitpic = models.CharField(max_length=160, default='/static/assets/images/logos/ARM_logo.png')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    HP = models.IntegerField(help_text='This units hitpoints', default=-1)
    size = models.CharField(max_length=160, help_text='The size of the unit i.e. 2x2', default='0x0')
    energyCost = models.IntegerField(help_text='The amount of energy this unit needs', default=-1)
    metalCost = models.IntegerField(help_text='The amount of metal this unit needs', default=-1)

    is_deleted = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    fbiSnowflake = models.CharField(max_length=160, null=True, blank=True)

    def __str__(self):
        return self.name