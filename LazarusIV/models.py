from django.db import models
from polymorphic.models import PolymorphicModel

from chat.models import JawnUser




class UploadRepository(models.Model):
    uploader = models.ForeignKey(JawnUser, on_delete=models.CASCADE, related_name='uploaded_by')
    title = models.CharField(max_length=100)
    total_units = models.IntegerField(default=0)
    current_worker_job = models.IntegerField(default=0)
    root_path = models.CharField(max_length=100)
    original_hpi_path = models.CharField(max_length=100)

class RepositoryDirectory(models.Model):
    dir_repository = models.ForeignKey(UploadRepository, on_delete=models.CASCADE, related_name='location')
    dir_name = models.CharField(max_length=100)
    dir_path = models.CharField(max_length=100)
    dir_total_files = models.IntegerField(default=0)

class RepositoryFile(models.Model):
    repo_dir = models.ForeignKey(RepositoryDirectory, on_delete=models.CASCADE, related_name='parent_folder')
    file_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)
    file_kind = models.CharField(max_length=100)
    file_thumbnail = models.CharField(max_length=100)

class BackgroundWorkerJob(models.Model):
    job_name = models.CharField(max_length=100)
    dispatched_by_repo = models.ForeignKey(UploadRepository, on_delete=models.CASCADE, related_name='the_repo_selector')
    is_finished = models.BooleanField(default=False)
    is_working = models.BooleanField(default=False)


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
