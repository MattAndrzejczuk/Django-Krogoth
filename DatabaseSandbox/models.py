from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class VisitorLogSB(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    remote_addr = models.CharField(max_length=255, blank=True, null=True)
    http_usr = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=255, blank=True, null=True)
    other_misc_notes = models.TextField(blank=True, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return "[%s]: %s" % self.http_usr % self.http_accept



FACTIONS = (
    ('Arm', 'Arm'),
    ('Core', 'Core'),
)
class LazarusCommanderAccountSB(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    is_suspended = models.BooleanField(default=False)
    is_terminated = models.BooleanField(default=False)
    faction = models.CharField(choices=FACTIONS, max_length=25)
    profile_pic = models.CharField(max_length=255)
    about_me = models.CharField(max_length=75)

    def __str__(self):              # __unicode__ on Python 2
        return "[%s]: %s" % faction % self.user.username



class LazarusModProjectSB(models.Model):
    unique_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    author = models.ForeignKey(User, unique=True)

    def __str__(self):              # __unicode__ on Python 2
        return "[%s]: %s" % self.unique_name % self.author.username



class BasicUploadTrackerSB(models.Model):
    file_name = models.CharField(max_length=100)
    download_url = models.CharField(max_length=255)
    system_path = models.CharField(max_length=255)
    author = models.CharField(max_length=255,blank=True, null=True)



class TotalAnnihilationUploadedFile(models.Model):
    file_name = models.CharField(max_length=100,help_text='Full name of this HPI/UFO file.')
    download_url = models.CharField(max_length=255,help_text='System path to this HPI/UFO file.')
    system_path = models.CharField(max_length=255,help_text='System path to the HPI extraction directory.')

    designation = models.CharField(max_length=255,
                                   blank=True,
                                   null=True,
                                   help_text='The pointer name to the parent Asset Upload Repository.')
    hpi_upload_id = models.CharField(max_length=255,
                                     blank=True,
                                     null=True,
                                     help_text='The id of the origin HPIUpload model.')
    uploader = models.CharField(max_length=255, blank=True, null=True)

    is_public = models.BooleanField(default=True)
    is_terminated = models.BooleanField(default=False)

    file_type = models.CharField(max_length=10)
    HPI_Extractor_Log = models.TextField(blank=True,
                                         null=True,
                                         help_text='The output result of EXE command that extracted this HPI/UFO.')

    def __str__(self):              # __unicode__ on Python 2
        return "%s" % self.file_name