import threading
import os
from LazarusIV.models import UploadRepository, BackgroundWorkerJob

EXTRACTION_ROOT = '/usr/src/persistent/media/user_uploads/'
DEFAULT_EXTRACTION_DESTINATION = 'FilesWithNoAuthor'
MAX_WORKERS = 1

class Worker():

    def __init__(self, repo_id: int):
        fresh_upload = UploadRepository.objects.get(id=repo_id)
        self.file_name_with_ext = ''
        self.extraction_directory = EXTRACTION_ROOT + DEFAULT_EXTRACTION_DESTINATION


    def workers_are_busy(self) -> bool:
        workers_currently_busy = BackgroundWorkerJob.objects.filter(is_working=True)
        if workers_currently_busy >= MAX_WORKERS:
            return True
        else:
            return False

    def get_next_worker_in_line(self) -> BackgroundWorkerJob:
        return BackgroundWorkerJob.objects.filter(is_finished=False).first()

    def order_worker_to_begin(self, worker: BackgroundWorkerJob):

        # TODO: I
        # JOB I
        def begin_hpi_dump(self, worker: BackgroundWorkerJob):
            fresh_upload = UploadRepository.objects.get(id=worker.dispatched_by_repo.id)

        # TODO: II
        # JOB II
        def rename_files_in_repo_to_lower(self, worker: BackgroundWorkerJob):
            fresh_upload = UploadRepository.objects.get(id=worker.dispatched_by_repo.id)

        if worker.job_name == 'I':
            threading.Thread(target=begin_hpi_dump, args=(worker, ))
        elif worker.job_name == 'II':
            threading.Thread(target=rename_files_in_repo_to_lower, args=(worker,))









    @property
    def get_bash_system_os_cmd(self):
        return "bash bashRenameStuffToLowerInDirectory_public.sh " + self.file_name_with_ext[:-4] + "/."



