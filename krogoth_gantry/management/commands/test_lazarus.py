
from django.core.management.base import BaseCommand

from LazarusIV.models import UploadRepository, RepositoryDirectory, RepositoryFile


import codecs
import os
from LazarusV.super_hpi.hpi_Z_debug import logged_disassembler
from jawn.settings import APP_VERSION

class Command(BaseCommand):
    help = 'prints the toolbar module and controller.'
    def add_arguments(self, parser):
        parser.add_argument('mvc_id', nargs="+", type=str)

    def handle(self, *args, **options):

        flake = 'ArmPrimeTest-0_v' + APP_VERSION
        repo_1 = UploadRepository.objects.get(id=1)
        test = logged_disassembler(repo_base=repo_1)
        print('ARGS: ')
        print(options)
        if options['mvc_id'][0] == "1":
            test.dump_all()
        elif options['mvc_id'][0] == "2":
            disass = test.core3_disassembler.filename_dictionary
            _str = test.json_pretty(disass)
            print(_str)
            print('\nfinished printing file origin paths.')

        elif options['mvc_id'][0] == "terminal_1":
            # I. PASSPORT PHASE

            rep0 = logged_disassembler.colored_orange('UploadRepository')
            rep1 = logged_disassembler.colored_blue(repo_1.title)
            rep2 = logged_disassembler.colored_green(repo_1.root_path)

            print(rep0)
            print('title: ' + rep1)
            print('root_path: ' + rep2)

            dirs = RepositoryDirectory.objects.filter(dir_repository=repo_1)
            d0 = logged_disassembler.colored_orange('RepositoryDirectory')
            print(d0)

            for dir in dirs:
                d1 = logged_disassembler.colored_purple(dir.dir_name)
                d2 = logged_disassembler.colored_green(str(dir.dir_total_files))
                print('[' + str(dir.id) + '] 📁 ' + d1 + ' ' + d2 + " total files.")
                try:
                    files = RepositoryFile.objects.filter(repo_dir=dir)
                    for file in files:
                        f1 = logged_disassembler.colored_blue(file.file_name)
                        f2 = logged_disassembler.colored_red(file.file_kind)
                        print('  └───────📜 ' + f1 + f2)
                except Exception as e:
                    print('  └───────⚠️ ')
                    print(e)


        elif options['mvc_id'][0] == "terminal_2":
            # II. CUSTOMS PHASE


            disass = test.core3_disassembler.filename_dictionary

            for key,val in disass.items():


                print(' ')
                print('', end=' 🔑 ')
                print(key)
                if val['kind'] == 'unit':
                    for unit in val['zdata']:



                        print('  ', end=' 🗝 ')
                        print(val['key_name'])
                        print('    ', end=' 📀 ')
                        print(str(unit)[0:65])
                elif val['kind'] == 'weapon':
                    for k,v in val['zdata'].items():



                        print('  ', end=' 🗝 ')
                        print(k)
                        print('    ', end=' 📀 ')
                        print(str(v)[0:65])
                elif val['kind'] == 'feature':
                    for k,v in val['zdata'].items():



                        print('  ', end=' 🗝 ')
                        print(k)
                        print('    ', end=' 📀 ')
                        print(str(v)[0:65])
                elif val['kind'] == 'download':
                    for k, v in val['zdata'].items():



                        print('  ', end=' 🗝 ')
                        print(k)
                        print('    ', end=' 📀 ')
                        print(str(v)[0:65])

                # print(str(val)[0:35])
                print(' ')
            print('\nfinished printing file origin paths.')
        elif options['mvc_id'][0] == "repo_to_cavedog_sql":
            pass
        elif options['mvc_id'][0] == "":
            pass
        elif options['mvc_id'][0] == "help":
            # print("show_repos")
            # print("repo_to_cavedog_sql")
            print("diss_repo_1")
            print("show_repo_1")
            # print("diss_repo_1")
            pass
