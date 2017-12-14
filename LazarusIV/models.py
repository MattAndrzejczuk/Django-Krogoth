from django.db import models
from django.core.validators import URLValidator
from chat.models import JawnUser
import os
# from jawn.settings import PUBLIC_EXTRACTED_HPIs, APP_VERSION
from PIL import Image, ImageDraw, ImageFont


PUBLIC_EXTRACTED_HPIs = ''
APP_VERSION = ''


import socket
from polymorphic.models import PolymorphicModel

class UploadRepository(models.Model):
    uploader = models.ForeignKey(JawnUser, on_delete=models.CASCADE, related_name='created_by')
    hpi_file = models.FileField(upload_to='uploaded_hpi_files/', help_text='Total Annihilation HPI, UFO or CCX file.')
    title = models.CharField(max_length=100)
    total_files = models.IntegerField(default=0)
    current_worker_job = models.IntegerField(default=0)
    root_path = models.CharField(max_length=100, help_text='The destination path this HPI file will be extracted to.')
    original_hpi_path = models.CharField(max_length=100)
    thumbnail_pic = models.CharField(max_length=100, default='NaN', validators=[URLValidator()])
    platform_version = models.CharField(max_length=90, default='Alpha v' + APP_VERSION)

    def __str__(self):
        return 'http://' + socket.gethostname() + self.thumbnail_pic.replace('/urs/src/persistent', '')


    @property
    def filename(self) -> str:
        return os.path.basename(self.hpi_file.name)

    @property
    def filename_no_ext(self) -> str:
        return os.path.basename(self.hpi_file.name)[:-4]

    @property
    def file_ext(self) -> str:
        return os.path.basename(self.hpi_file.name)[-4:]

    @property
    def filepath(self) -> str:
        return self.hpi_file.path

    def save(self, *args, **kwargs):
        print(' 💾 🗄 ')
        super(UploadRepository, self).save(*args, **kwargs)

    def make_first_thumbnail(self):
        output_save_path = '/usr/src/persistent/media/Generated_Thumbnails/'
        bgimg = Image.open('./png_generator/background.png')
        txt = Image.new('RGBA', bgimg.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype('./static/fonts/Haettenschweiler.ttf', 40)
        d = ImageDraw.Draw(txt)
        d.text((10, 10), 'REPOSITORY', font=fnt, fill=(155, 155, 155, 178))
        out = Image.alpha_composite(bgimg, txt)
        out.save(output_save_path + self.title + '.png')
        self.thumbnail_pic = output_save_path + self.title + '.png'
        self.save()

    def make_second_thumbnail(self):
        total_files = len(os.listdir(self.root_path))
        self.total_files = total_files
        output_save_path = '/usr/src/persistent/media/Generated_Thumbnails/'
        bgimg = Image.open('./png_generator/background.png')
        txt = Image.new('RGBA', bgimg.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype('./static/fonts/Haettenschweiler.ttf', 40)
        d = ImageDraw.Draw(txt)
        d.text((10, 10), 'REPOSITORY', font=fnt, fill=(155, 215, 155, 218))
        d.text((10, 60), str(total_files) + ' files', font=fnt, fill=(155, 55, 55, 235))
        out = Image.alpha_composite(bgimg, txt)
        out.save(output_save_path + self.title + '.png')
        self.thumbnail_pic = output_save_path + self.title + '.png'
        self.save()

    def set_file_paths(self):
        self.original_hpi_path = self.filepath
        username = self.uploader.base_user.username
        self.root_path = PUBLIC_EXTRACTED_HPIs + username + '/' + self.filename_no_ext + '/'
        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)


        self.save()


JOB_TYPES = (
        ('I', 'I. Dump HPI Contents'),
        ('II', 'II. Rename Files To Lowercase'),
        ('III', 'III. Process Dump Using SuperHPI'),
    )
class BackgroundWorkerJob(models.Model):

    job_name = models.CharField(max_length=100, choices=JOB_TYPES)
    dispatched_by_repo = models.ForeignKey(UploadRepository,
                                           on_delete=models.CASCADE,
                                           related_name='the_repo_selector',
                                           null=True)
    is_finished = models.BooleanField(default=False)
    is_working = models.BooleanField(default=False)

    @property
    def parent_user(self):
        return self.dispatched_by_repo.uploader

    def save(self, *args, **kwargs):
        print(' 💾 🤖 ')
        super(BackgroundWorkerJob, self).save(*args, **kwargs)

    def enqueue_job(self, on_repo: UploadRepository, to_do: str):
        self.dispatched_by_repo = on_repo
        self.job_name = to_do
        self.save()

# Some large job starts being executed:
    def set_as_busy(self):
        self.is_working = True
        self.save()


REPO_DIR_TYPES = (
        ('Master', 'Master Path'),
        ('Data', 'Data Dependencies'),
        ('File', 'File Dependencies'),
        ('Misc', 'Non Dependencies, optional content like menu bitmaps'),
    )
class RepositoryDirectory(models.Model):
    dir_repository = models.ForeignKey(UploadRepository, on_delete=models.CASCADE, related_name='location', null=True)
    dir_name = models.CharField(max_length=100)
    dir_path = models.CharField(max_length=201)
    dir_total_files = models.IntegerField(default=0)
    dir_kind = models.CharField(max_length=100, choices=REPO_DIR_TYPES, default='Misc')

    def save(self, *args, **kwargs):
        print(' 💾 📁 ')
        super(RepositoryDirectory, self).save(*args, **kwargs)

    def save_master_path(self, name: str, full_path: str):
        self.dir_name = name
        self.dir_path = full_path
        self.dir_total_files = len(os.listdir(full_path))
        self.dir_kind = 'Master'


    def save_root_path(self, name: str, full_path: str):
        self.dir_name = name
        self.dir_path = full_path
        self.dir_total_files = len(os.listdir(full_path))
        self.dir_kind = 'Data'


class RepositoryFile(PolymorphicModel):
    repo_dir = models.ForeignKey(RepositoryDirectory, on_delete=models.CASCADE, related_name='parent_folder', null=True)
    file_name = models.CharField(max_length=101)
    file_path = models.CharField(max_length=202)
    file_kind = models.CharField(max_length=103)
    file_thumbnail = models.CharField(max_length=104)

    def __str__(self):
        return self.file_name + ', ' + self.file_path + ', ' + self.file_kind + ', ' + self.file_thumbnail + ', '

    def save(self, *args, **kwargs):
        print(' 💾 📄 ')
        super(RepositoryFile, self).save(*args, **kwargs)

    def save_as_file(self, filename: str, path: str, repodir_id: int):
        self.file_kind = filename[-4:]
        self.file_name = filename[:-4]
        self.file_path = path
        self.repo_dir = RepositoryDirectory.objects.get(id=repodir_id)
        self.file_thumbnail = 'NaN'
        # self.save()

        output_save_path = '/usr/src/persistent/media/Generated_Thumbnails/'
        bgimg = Image.open('./png_generator/background.png')
        txt = Image.new('RGBA', bgimg.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype('./static/fonts/Haettenschweiler.ttf', 40)
        d = ImageDraw.Draw(txt)
        d.text((10, 10), self.file_kind, font=fnt, fill=(155, 155, 155, 178))
        file_contents = open(self.file_path, 'r', errors='replace')
        raw = '{...}'

        fnt_sml = ImageFont.truetype('./static/fonts/Haettenschweiler.ttf', 12)
        if self.file_kind == '.fbi':
            raw = file_contents.read()
            d.text((10, 60), raw, font=fnt_sml, fill=(55, 55, 155, 235))
        elif self.file_kind == '.tdf':
            raw = file_contents.read()
            d.text((10, 60), raw, font=fnt_sml, fill=(155, 55, 55, 235))
        else:
            d.text((10, 60), raw, font=fnt, fill=(55, 95, 55, 235))

        out = Image.alpha_composite(bgimg, txt)
        out.save(output_save_path + self.file_name + self.file_kind + '|' + str(self.repo_dir.id) + '.png')
        self.file_thumbnail = '/media/Generated_Thumbnails/' + self.file_name + self.file_kind + '|' + str(
                self.repo_dir.id) + '.png'
        # self.save()


        # self.file_kind = 'Junk|' + filename[-4:]
        # self.save()

class RepositoryFileGeneric(RepositoryFile):
    is_junk = models.BooleanField(default=True,
                                  help_text='Junk will be deleted monthly by a daemon process. When verifying ' +
                                            'dependencies, this must be set to True if it will be used for mods.')
    def save_junk_file(self, filename: str, path: str, repodir_id: int):
        self.save_as_file(filename=filename, path=path, repodir_id=repodir_id)

class RepositoryFileTAData(RepositoryFileGeneric):
    is_approved = models.BooleanField(default=False,
                                      help_text='Approved by AssetTerminalArrivals.Customs if this TDF or FBI file is not corrupted.')
    status = models.CharField(default='awaiting customs response certificate...', max_length=202)

class RepositoryFileReadOnly(RepositoryFileGeneric):
    file_size = models.IntegerField(default=-1, help_text='Size is -1 if it is unknown.')

class NotificationCenter(models.Model):
    parent_user = models.OneToOneField(JawnUser, related_name='armprime_user', on_delete=models.CASCADE)
    unread_private = models.IntegerField(default=0)

class NotificationItem(models.Model):
    center = models.ForeignKey(NotificationCenter, on_delete=models.CASCADE, related_name='notifier')
    is_private = models.BooleanField(default=True)
    kind = models.CharField(max_length=250)
    image_url = models.CharField(max_length=250)
    sfx_chime = models.CharField(max_length=250)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    unread = models.CharField(max_length=250) #TODO: should be a Bool?

    def save(self, *args, **kwargs):
        # TODO: WebSocket or FireBase is called here.
        super(NotificationItem, self).save(*args, **kwargs)
