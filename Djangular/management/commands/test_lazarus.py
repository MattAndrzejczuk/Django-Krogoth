
from django.core.management.base import BaseCommand


from Djangular.models import DjangularMasterViewController, DjangularIcon, DjangularService, \
    DjangularCategory, DjangularSlaveViewController, DjangularDirective
import codecs
import os
from LazarusV.super_hpi.hpi_Z_debug import logged_disassembler
from jawn.settings import APP_VERSION

class Command(BaseCommand):
    help = 'prints the toolbar module and controller.'
    def add_arguments(self, parser):
        parser.add_argument('mvc_id', nargs="+", type=int)

    def handle(self, *args, **options):

        flake = 'ArmPrimeTest' + APP_VERSION
        test = logged_disassembler()
        print('ARGS: ')
        print(options)
        if options['mvc_id'][0] == 1:
            test.dump_all()
        elif options['mvc_id'][0] == 2:
            disass = test.core3_disassembler.filename_dictionary
            _str = test.json_pretty(disass)
            print(_str)
            print('\nfinished printing file origin paths.')
        elif options['mvc_id'][0] == 3:
            disass = test.core3_disassembler.filename_dictionary
            for key,val in disass.items():
                print(' ')
                print('', end=' 🔑 ')
                print(key)
                # print('┣━━━━━━━━━━━━━━━━━━━━┫')
                # print('╻', end=' 💿 ')
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
        elif options['mvc_id'] == 4:
            pass
        elif options['mvc_id'] == 5:
            pass
        elif options['mvc_id'] == 6:
            pass
        elif options['mvc_id'] == 7:
            pass

