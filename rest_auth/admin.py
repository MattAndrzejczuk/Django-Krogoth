# from django.contrib import admin

# Register your models here.

# from LazarusIV.models import UploadRepository, RepositoryDirectory, RepositoryFile
# from LazarusV.super_hpi.hpi_Z_debug import logged_disassembler
# repo_1 = UploadRepository.objects.get(id=1)
# test = logged_disassembler(repo_base=repo_1)
# dirs = RepositoryDirectory.objects.filter(dir_repository=repo_1)
# for dir in dirs:
#     files = RepositoryFile.objects.filter(repo_dir=dir)
#     for file in files:
#         f1 = logged_disassembler.colored_blue(file.file_name)
#         f2 = logged_disassembler.colored_red(file.file_kind)
#         print('  └───────📜 ' + f1 + f2)

# from LazarusIV.models import UploadRepository, RepositoryDirectory, RepositoryFile
# from LazarusV.super_hpi.hpi_Z_debug import logged_disassembler
# repo_1 = UploadRepository.objects.get(id=1)
# test = logged_disassembler(repo_base=repo_1)
# dirs = RepositoryDirectory.objects.filter(dir_repository=repo_1)
# for dir in dirs:
#     print(dir)
#     files = RepositoryFile.objects.filter(repo_dir=dir)
#     for file in files:
#         print(file)
