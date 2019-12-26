import os

from django.core.management.base import BaseCommand
from krogoth_gantry.helpers.kolors import ink

class Command(BaseCommand):
    help = 'prints the information about environment variables i.e. Redis host address, SQL password, etc...'
    
    def add_arguments(self, parser):
        parser.add_argument('--foo', nargs="+", type=str)
        parser.add_argument('--bar', nargs="+", type=str)
    # print(options["mvc_id"][0])
    def handle(self, *args, **options):
        ink.pgreen("\n options ")
        ink.pred("'--foo'")
        ink.pblue(options["foo"])
        ink.pred("'--bar'")
        ink.pblue(options["bar"])
        print()