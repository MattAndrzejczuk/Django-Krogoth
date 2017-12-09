import threading
import time
import os
from LazarusIV.models import UploadRepository, BackgroundWorkerJob, RepositoryDirectory, RepositoryFile, \
    RepositoryFileGeneric, RepositoryFileTAData, RepositoryFileReadOnly
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
        print(' 👞💢🐂 ', end='')
        if self.workers_are_busy == False:
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
        print(' ⛓ ', end='')

        # JOB I
        def dispatch_hpi_dump(worker_id: int):
            worker = BackgroundWorkerJob.objects.get(id=worker_id)
            cmd = 'bash extractTA_Mod.sh ' + worker.dispatched_by_repo.original_hpi_path \
                  + ' ' + worker.dispatched_by_repo.root_path
            # print(cmd)
            os.system(cmd)
            print(' 🔨 ', end='')
            worker.is_working = False
            worker.is_finished = True
            worker.save()
            print(' I ✅ ')
            replace_with_next_job = BackgroundWorkerJob()
            replace_with_next_job.enqueue_job(on_repo=worker.dispatched_by_repo, to_do='II')

        # JOB II
        def dispatch_rename_files_lower(worker_id: int):
            worker = BackgroundWorkerJob.objects.get(id=worker_id)
            cmd = "bash bashRenameStuffToLowerInDirectory_public.sh " + worker.dispatched_by_repo.root_path + "."
            # print(cmd)
            os.system(cmd)
            print(' 🔧 ', end='')
            worker.is_working = False
            worker.is_finished = True
            worker.save()
            print(' II ✅ ')
            replace_with_next_job = BackgroundWorkerJob()
            replace_with_next_job.enqueue_job(on_repo=worker.dispatched_by_repo, to_do='III')

        # JOB III
        def dispatch_scan_repository_directories(worker_id: int):
            worker = BackgroundWorkerJob.objects.get(id=worker_id)
            repo_contents = os.listdir(worker.dispatched_by_repo.root_path)
            master_repo_dir = RepositoryDirectory(dir_repository=worker.dispatched_by_repo)
            master_repo_dir.save_master_path(full_path=worker.dispatched_by_repo.root_path, name=worker.dispatched_by_repo.title)
            master_repo_dir.save()
            for path in repo_contents:
                if os.path.isdir(worker.dispatched_by_repo.root_path + path):
                    new_repo_dir = RepositoryDirectory(dir_repository=worker.dispatched_by_repo)
                    new_repo_dir.save_root_path(name=path, full_path=worker.dispatched_by_repo.root_path + path)
                    new_repo_dir.save()
                elif os.path.isfile(worker.dispatched_by_repo.root_path + path):
                    new_junk_file = RepositoryFileGeneric()
                    new_junk_file.save_junk_file(path=worker.dispatched_by_repo.root_path + path,
                                                 filename=path,
                                                 repodir_id=master_repo_dir.id)
                    new_junk_file.save()

            print(' 🔧 ', end='')
            worker.is_working = False
            worker.is_finished = True
            ping = Notifier(for_user=worker.parent_user)
            ping.ping_basic_alert(msg='JOB III completed!')
            worker.save()
            print(' III ✅ ')
            replace_with_next_job = BackgroundWorkerJob()
            replace_with_next_job.enqueue_job(on_repo=worker.dispatched_by_repo, to_do='IV')

        # JOB IV
        def dispatch_scan_repository_files(worker_id: int):
            # TODO: move code below to a new class called: AssetTerminalArrivals.PhaseI_CheckPassport
            worker = BackgroundWorkerJob.objects.get(id=worker_id)
            repo_dirs = RepositoryDirectory.objects.filter(dir_repository=worker.dispatched_by_repo)
            for dir in repo_dirs:
                contents = os.listdir(dir.dir_path)
                for content in contents:
                    if content == 'corpses':
                        new_repo_dir = RepositoryDirectory(dir_repository=worker.dispatched_by_repo)
                        new_repo_dir.save_root_path(name='corpses', full_path=dir.dir_path + '/corpses/')
                        new_repo_dir.save()
                        corpse_files = os.listdir(dir.dir_path + '/corpses/')
                        for tdf in corpse_files:
                            if os.path.isfile(dir.dir_path + '/corpses/' + tdf):
                                new_file = RepositoryFileTAData()
                                new_file.save_as_file(filename=tdf, path=dir.dir_path + '/corpses/' + tdf, repodir_id=new_repo_dir.id)
                                new_file.save()
                    else:
                        new_file = RepositoryFileGeneric()
                        if dir.dir_name == 'units' or dir.dir_name == 'download' or dir.dir_name == 'weapons':
                            new_file = RepositoryFileTAData()
                        else:
                            new_file = RepositoryFileReadOnly()
                        if os.path.isfile(dir.dir_path + '/' + content):
                            new_file.save_as_file(filename=content, path=dir.dir_path + '/' + content, repodir_id=dir.id)
                            new_file.save()
            ping = Notifier(for_user=worker.parent_user)
            ping.ping_basic_alert(msg='JOB IV completed!')
            worker.is_working = False
            worker.is_finished = True
            worker.save()
            print(' IV ✅ ')
            # AssetTerminalArrivals.PhaseII_Customs
            # AssetTerminalArrivals.PhaseIII_Depart

        # JOB V
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
            ping.ping_basic_alert(msg='JOB V completed!')
            worker.is_working = False
            worker.is_finished = True
            worker.save()
            print(' V ✅ ')

        if worker.job_name == 'I':
            worker.set_as_busy()
            run_thread = threading.Thread(target=dispatch_hpi_dump, args=(worker.id,))
            run_thread.start()
        elif worker.job_name == 'II':
            worker.set_as_busy()
            run_thread = threading.Thread(target=dispatch_rename_files_lower, args=(worker.id,))
            run_thread.start()
        elif worker.job_name == 'III':
            worker.set_as_busy()
            worker.dispatched_by_repo.make_first_thumbnail()
            run_thread = threading.Thread(target=dispatch_scan_repository_directories, args=(worker.id,))
            run_thread.start()
        elif worker.job_name == 'IV':
            worker.set_as_busy()
            worker.dispatched_by_repo.make_second_thumbnail()
            run_thread = threading.Thread(target=dispatch_scan_repository_files, args=(worker.id,))
            run_thread.start()



    def get_bash_system_os_cmd(self):
        return "bash bashRenameStuffToLowerInDirectory_public.sh " + self.file_name_with_ext[:-4] + "/."
