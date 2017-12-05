from django.db import models
from chat.models import JawnUser
import os
from jawn.settings import PUBLIC_EXTRACTED_HPIs
from PIL import Image, ImageDraw, ImageFont



class UploadRepository(models.Model):
    uploader = models.ForeignKey(JawnUser, on_delete=models.CASCADE, related_name='created_by')
    hpi_file = models.FileField(upload_to='uploaded_hpi_files/', help_text='Total Annihilation HPI, UFO or CCX file.')
    title = models.CharField(max_length=100)
    total_units = models.IntegerField(default=0)
    current_worker_job = models.IntegerField(default=0)
    root_path = models.CharField(max_length=100, help_text='The destination path this HPI file will be extracted to.')
    original_hpi_path = models.CharField(max_length=100)
    thumbnail_pic = models.CharField(max_length=100, default='NaN')

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
# I. FINISHED:
    def extraction_did_complete(self):
        # self.is_working = False
        # self.is_finished = True
        # self.dispatched_by_repo.hpi_extraction_did_finish()
        # self.save()
        replace_with_next_job = BackgroundWorkerJob()
        replace_with_next_job.enqueue_job(on_repo=self.dispatched_by_repo, to_do='II')
# II. FINISHED:
    def rename_did_complete(self):
        # self.is_working = False
        # self.is_finished = True
        # self.save()
        replace_with_next_job = BackgroundWorkerJob()
        replace_with_next_job.enqueue_job(on_repo=self.dispatched_by_repo, to_do='III')
# III. FINISHED:
    def super_hpi_did_complete(self):
        self.is_working = False
        self.is_finished = True
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


class RepositoryFile(models.Model):
    repo_dir = models.ForeignKey(RepositoryDirectory, on_delete=models.CASCADE, related_name='parent_folder', null=True)
    file_name = models.CharField(max_length=101)
    file_path = models.CharField(max_length=202)
    file_kind = models.CharField(max_length=103)
    file_thumbnail = models.CharField(max_length=104)

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
        bgimg = Image.open('./png_generator/background.png')
        txt = Image.new('RGBA', bgimg.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype('./static/fonts/Haettenschweiler.ttf', 40)
        d = ImageDraw.Draw(txt)
        d.text((10, 10), self.file_kind, font=fnt, fill=(255, 255, 255, 178))

        if self.file_kind == '.fbi':
            file_contents = open(self.file_path, 'r', errors='replace')
            raw = file_contents.read()
            d.text((10, 60), raw[0:15], font=fnt, fill=(255, 255, 255, 235))
            out = Image.alpha_composite(bgimg, txt)
            out.save('Generated_Thumbnails/' + self.file_name + self.file_kind + str(self.id))
            self.file_thumbnail = 'Generated_Thumbnails/' + self.file_name + self.file_kind + str(self.id)
        elif self.file_kind == '.tdf':
            file_contents = open(self.file_path, 'r', errors='replace')
            raw = file_contents.read()
            d.text((10, 60), raw[0:15], font=fnt, fill=(255, 255, 255, 235))
            out = Image.alpha_composite(bgimg, txt)
            out.save('Generated_Thumbnails/' + self.file_name + self.file_kind + str(self.id))
            self.file_thumbnail = 'Generated_Thumbnails/' + self.file_name + self.file_kind + str(self.id)
        # self.save()

    def save_junk_file(self, filename: str, path: str, repodir_id: int):
        self.save_as_file(filename=filename, path=path, repodir_id=repodir_id)
        # self.file_kind = 'Junk|' + filename[-4:]
        # self.save()



class NotificationCenter(models.Model):
    parent_user = models.OneToOneField(JawnUser, related_name='armprime_user', )
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
