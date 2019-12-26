import os
from krogoth_gantry.helpers.stores.make_from_scaffold import NewLazyMVC
from django.core.management.base import BaseCommand
from krogoth_gantry.helpers.kolors import ink


class Command(BaseCommand):
    help = 'prints the information about environment variables i.e. Redis host address, SQL password, etc...'

    def add_arguments(self, parser):
        parser.add_argument('--name', nargs="+", type=str)
        parser.add_argument('--tmpl', nargs="+", type=str)
        parser.add_argument('--info', nargs="+", type=str)
        parser.add_argument('--examples', nargs="+", type=str)

    # print(options["mvc_id"][0])
    def handle(self, *args, **options):
        if options["info"] is not None:
            ink.pbluelight('--name ')
            ink.pgreen('unique name for qube \n')
            ink.pbluelight('--tmpl ')
            ink.pgreen('"lazy" \n')
        elif options["examples"] is not None:
            n1 = 'lazy_example'
            s1 = 'lazy'
            ink.pred('\nEXAMPLES: \n')
            ink.pgreen('\n ./manage.py krogoth_make_qube --name "' + n1 + '" --tmpl ' + s1 + ' \n')
        else:
            name = options["name"][0]
            NewLazyMVC(name=name, main_dir='No_Cat', sub_dir='No_Subcat')
            print("OK")
