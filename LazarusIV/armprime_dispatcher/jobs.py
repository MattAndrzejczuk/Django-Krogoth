import threading
import os
from LazarusIV.models import UploadRepository

EXTRACTION_ROOT = '/usr/src/persistent/media/user_uploads/'
DEFAULT_EXTRACTION_DESTINATION = 'FilesWithNoAuthor'

class UploadProcessor():

    def __init__(self, repo_id: int):
        fresh_upload = UploadRepository.objects.get(id=repo_id)
        self.file_name_with_ext = ''
        self.extraction_directory = EXTRACTION_ROOT + DEFAULT_EXTRACTION_DESTINATION

    @property
    def get_bash_system_os_cmd(self):
        return "bash bashRenameStuffToLowerInDirectory_public.sh " + self.file_name_with_ext[:-4] + "/."

    @classmethod
    def rename_files_in_repo_to_lower(self, repo_id: int):
        fresh_upload = UploadRepository.objects.get(id=repo_id)
