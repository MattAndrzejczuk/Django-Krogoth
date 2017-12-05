import threading
import time
import os
from LazarusIV.models import UploadRepository, BackgroundWorkerJob
from LazarusIV.armprime_dispatcher.notifications import Notifier

EXTRACTION_ROOT = '/usr/src/persistent/media/user_uploads/'
DEFAULT_EXTRACTION_DESTINATION = 'FilesWithNoAuthor'
MAX_WORKERS = 1

class Worker():

    def __init__(self):
        print(' 🤖 ', end='')
        self.file_name_with_ext = ''
        self.extraction_directory = EXTRACTION_ROOT + DEFAULT_EXTRACTION_DESTINATION


    def kickThatMuleLee(self):
        if self.workers_are_busy == False:
            print('WORKERS STARTING...')
            first_inline = self.get_next_worker_in_line
            if first_inline is not None:
                self.order_worker_to_begin(worker=first_inline)
        else:
            print('workers sleeping...')
            pass


    @property
    def workers_are_busy(self) -> bool:
        workers_currently_busy = BackgroundWorkerJob.objects.filter(is_working=True)
        if len(workers_currently_busy) >= MAX_WORKERS:
            print(' ⏳️  🛑 ')
            return True
        else:

            return False

    @property
    def get_next_worker_in_line(self) -> BackgroundWorkerJob:
        return BackgroundWorkerJob.objects.filter(is_finished=False).first()

    def order_worker_to_begin(self, worker: BackgroundWorkerJob):
        print(' 🏁 ', end='')
        print('worker next in line: ' + str(worker.id))

        # JOB I
        def dispatch_hpi_dump(worker_id: int):
            time.sleep(2)
            worker = BackgroundWorkerJob.objects.get(id=worker_id)
            cmd = 'bash extractTA_Mod.sh ' + worker.dispatched_by_repo.original_hpi_path \
                  + ' ' + worker.dispatched_by_repo.root_path
            print(cmd)
            os.system(cmd)
            print(' 🔨 ', end='')
            worker.is_working = False
            worker.is_finished = True
            worker.save()
            replace_with_next_job = BackgroundWorkerJob()
            replace_with_next_job.enqueue_job(on_repo=worker.dispatched_by_repo, to_do='II')

        # JOB II
        def dispatch_rename_files_lower(worker_id: int):
            time.sleep(2)
            worker = BackgroundWorkerJob.objects.get(id=worker_id)
            cmd = "bash bashRenameStuffToLowerInDirectory_public.sh " + worker.dispatched_by_repo.root_path + "."
            print(cmd)
            # os.system(cmd)
            print(' 🔧 ', end='')
            worker.is_working = False
            worker.is_finished = True
            worker.save()

        # JOB III
        def dispatch_first_super_hpi_scan(worker_id: int):
            # TODO: SuperHPI - Menu Option 30.
            ## SuperHPI should generate png thumbnails
            ## should load all unit assets into RAM as Dict and Array
            ## RETURNS:
            ## -> cavedog_data_base  AS  RepositoryFile>-<CavedogBase
            ## -> all_readonly_assets  AS  RepositoryFile
            # TODO: SuperHPI - Menu Option [9, 2, 11] is for the publisher.
            worker = BackgroundWorkerJob.objects.get(id=worker_id)
            ping = Notifier(for_user=worker.parent_user)
            ping.ping_basic_alert(msg='JOB III completed!')
            worker.is_working = False
            worker.is_finished = True
            worker.save()

        worker.set_as_busy()
        if worker.job_name == 'I':
            run_thread = threading.Thread(target=dispatch_hpi_dump, args=(worker.id,))
            run_thread.start()
        elif worker.job_name == 'II':
            run_thread = threading.Thread(target=dispatch_rename_files_lower, args=(worker.id,))
            run_thread.start()
        elif worker.job_name == 'III':
            run_thread = threading.Thread(target=dispatch_first_super_hpi_scan, args=(worker.id,))
            run_thread.start()


    def get_bash_system_os_cmd(self):
        return "bash bashRenameStuffToLowerInDirectory_public.sh " + self.file_name_with_ext[:-4] + "/."
