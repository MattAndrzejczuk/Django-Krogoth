import threading
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
            first_inline = self.get_next_worker_in_line
            self.order_worker_to_begin(worker=first_inline)
        else:
            pass


    @property
    def workers_are_busy(self) -> bool:
        workers_currently_busy = BackgroundWorkerJob.objects.filter(is_working=True)
        if workers_currently_busy >= MAX_WORKERS:
            print(' ⏳️  🛑 ')
            return True
        else:
            return False

    @property
    def get_next_worker_in_line(self) -> BackgroundWorkerJob:
        return BackgroundWorkerJob.objects.filter(is_finished=False).first()

    def order_worker_to_begin(self, worker: BackgroundWorkerJob):
        print(' 🏁 ', end='')


        # JOB I
        def dispatch_hpi_dump(self, worker: BackgroundWorkerJob):
            # TODO: extractTA_Mod.sh
            print(' 🔨 ', end='')
            worker.extraction_did_complete()


        # JOB II
        def dispatch_rename_files_lower(self, worker: BackgroundWorkerJob):
            # TODO: bashRenameStuffToLowerInDirectory_public.sh
            print(' 🔧 ', end='')
            worker.rename_did_complete()

        # JOB III
        def dispatch_first_super_hpi_scan(self, worker: BackgroundWorkerJob):
            # TODO: SuperHPI - Menu Option 3
            ## SuperHPI should generate png thumbnails
            ## should load all unit assets into RAM as Dict and Array
            ## RETURNS:
            ## -> cavedog_data_base  AS  RepositoryFile>-<CavedogBase
            ## -> all_readonly_assets  AS  RepositoryFile
            # TODO: SuperHPI - Menu Option [9, 2, 11] is for the publisher.
            ping = Notifier(for_user=worker.parent_user)
            ping.ping_basic_alert(msg='JOB III completed!')


        # JOB IV
        def dispatch_generate_png_thumbnails(self, worker: BackgroundWorkerJob):
            # TODO: bashRenameStuffToLowerInDirectory_public.sh
            print(' 🔧 ', end='')
            worker.rename_did_complete()


        if worker.job_name == 'I':
            worker.set_as_busy()
            threading.Thread(target=dispatch_hpi_dump, args=(worker, ))
        elif worker.job_name == 'II':
            worker.set_as_busy()
            threading.Thread(target=dispatch_rename_files_lower, args=(worker,))
        elif worker.job_name == 'III':
            worker.set_as_busy()
            threading.Thread(target=dispatch_first_super_hpi_scan, args=(worker,))
        elif worker.job_name == 'IV':
            worker.set_as_busy()
            threading.Thread(target=dispatch_first_super_hpi_scan, args=(worker,))
        else:
            print('UNKOWN JOB WAS ASSIGNED TO WORKER ! ! !')





    def get_bash_system_os_cmd(self):
        return "bash bashRenameStuffToLowerInDirectory_public.sh " + self.file_name_with_ext[:-4] + "/."



