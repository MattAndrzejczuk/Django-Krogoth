import threading
import os
from LazarusIV.models import UploadRepository, BackgroundWorkerJob

EXTRACTION_ROOT = '/usr/src/persistent/media/user_uploads/'
DEFAULT_EXTRACTION_DESTINATION = 'FilesWithNoAuthor'
MAX_WORKERS = 1

class Worker():

    def __init__(self, repo_id: int):
        print(' 🤖 ', end='')
        fresh_upload = UploadRepository.objects.get(id=repo_id)
        self.file_name_with_ext = ''
        self.extraction_directory = EXTRACTION_ROOT + DEFAULT_EXTRACTION_DESTINATION


    def workers_are_busy(self) -> bool:
        workers_currently_busy = BackgroundWorkerJob.objects.filter(is_working=True)
        if workers_currently_busy >= MAX_WORKERS:
            print(' ⏳️  🛑 ')
            return True
        else:
            return False

    def get_next_worker_in_line(self) -> BackgroundWorkerJob:
        return BackgroundWorkerJob.objects.filter(is_finished=False).first()

    def order_worker_to_begin(self, worker: BackgroundWorkerJob):
        print(' 🏁 ', end='')

        # TODO: I
        # JOB I
        def dispatch_hpi_dump(self, worker: BackgroundWorkerJob):
            fresh_upload = UploadRepository.objects.get(id=worker.dispatched_by_repo.id)
            print(' 🔨 ', end='')

        # TODO: II
        # JOB II
        def dispatch_rename_files_lower(self, worker: BackgroundWorkerJob):
            fresh_upload = UploadRepository.objects.get(id=worker.dispatched_by_repo.id)
            print(' 🔧 ', end='')

        if worker.job_name == 'I':
            threading.Thread(target=dispatch_hpi_dump, args=(worker, ))
        elif worker.job_name == 'II':
            threading.Thread(target=dispatch_rename_files_lower, args=(worker,))





    def get_bash_system_os_cmd(self):
        return "bash bashRenameStuffToLowerInDirectory_public.sh " + self.file_name_with_ext[:-4] + "/."



