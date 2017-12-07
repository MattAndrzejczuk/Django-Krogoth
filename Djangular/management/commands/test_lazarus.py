
from django.core.management.base import BaseCommand


from Djangular.models import DjangularMasterViewController, DjangularIcon, DjangularService, \
    DjangularCategory, DjangularSlaveViewController, DjangularDirective
import codecs
import os
from LazarusV.super_hpi.hpi_Z_debug import logged_disassembler


class Command(BaseCommand):
    help = 'prints the toolbar module and controller.'
    def add_arguments(self, parser):
        parser.add_argument('mvc_id', nargs="+", type=int)

    def handle(self, *args, **options):

        test = logged_disassembler()
        print('ARGS: ')
        print(options)
        if options['mvc_id'][0] == 1:
            test.dump_all()
        elif options['mvc_id'][0] == 2:
            disass = test.core3_disassembler.filename_dictionary
            str = test.json_pretty(disass)
            print(str)
            print('\nfinished printing file origin paths.')
        elif options['mvc_id'] == 3:
            pass
        elif options['mvc_id'] == 4:
            pass
        elif options['mvc_id'] == 5:
            pass
        elif options['mvc_id'] == 6:
            pass
        elif options['mvc_id'] == 7:
            pass

