from django.db import models
from chat.models import JawnUser
import os






class UploadRepository(models.Model):
    uploader = models.ForeignKey(JawnUser, on_delete=models.CASCADE, related_name='created_by')
    hpi_file = models.FileField(upload_to='uploaded_hpi_files/', help_text='Total Annihilation HPI, UFO or CCX file.')
    title = models.CharField(max_length=100)
    total_units = models.IntegerField(default=0)
    current_worker_job = models.IntegerField(default=0)
    root_path = models.CharField(max_length=100, help_text='The destination path this HPI file will be extracted to.')
    original_hpi_path = models.CharField(max_length=100)

    @property
    def filename(self) -> str:
        return os.path.basename(self.hpi_file.name)

    @property
    def filepath(self) -> str:
        return self.hpi_file.path

    def set_file_paths(self):
        self.original_hpi_path = self.filepath
        self.root_path = self.filepath.replace(self.filename, '')
        self.save()


class BackgroundWorkerJob(models.Model):
    JOB_TYPES = (
        ('I', 'I. Dump HPI Contents'),
        ('II', 'II. Rename Files To Lowercase'),
        ('III', 'III. Convert PCX Files To PNG'),
        ('IV', 'IV. Process Dump Using SuperHPI'),
    )
    job_name = models.CharField(max_length=100, choices=JOB_TYPES)
    dispatched_by_repo = models.ForeignKey(UploadRepository,
                                           on_delete=models.CASCADE,
                                           related_name='the_repo_selector',
                                           null=True)
    is_finished = models.BooleanField(default=False)
    is_working = models.BooleanField(default=False)

    def enqueue_hpi_dump_job(self, on_repo: UploadRepository):
        self.dispatched_by_repo = on_repo
        self.job_name = 'I'
        self.save()


class RepositoryDirectory(models.Model):
    dir_repository = models.ForeignKey(UploadRepository, on_delete=models.CASCADE, related_name='location', null=True)
    dir_name = models.CharField(max_length=100)
    dir_path = models.CharField(max_length=100)
    dir_total_files = models.IntegerField(default=0)

class RepositoryFile(models.Model):
    repo_dir = models.ForeignKey(RepositoryDirectory, on_delete=models.CASCADE, related_name='parent_folder', null=True)
    file_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)
    file_kind = models.CharField(max_length=100)
    file_thumbnail = models.CharField(max_length=100)


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
    unread = models.CharField(max_length=250)
