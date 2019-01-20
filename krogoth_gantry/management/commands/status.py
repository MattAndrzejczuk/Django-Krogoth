import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'prints the information about environment variables i.e. Redis host address, SQL password, etc...'
    
    # def add_arguments(self, parser):
    #     parser.add_argument('mvc_id', nargs="+", type=str)
    # print(options["mvc_id"][0])
    def handle(self, *args, **options):
        red = '\033[31m'
        ENDC = '\033[0m'
        lightblue = '\033[94m'
        print(
            '\033[33m' + "\n\nTO USE THE PYCHARM DJANGO CONSOLE, ADD THIS TO THE TOP OF THE STARTING SCRIPT: \n\n\n" + ENDC)
        print("import os")
        print("os.environ = {}")
        for k, v in os.environ.items():
            os.environ[k] = v
            print("os.environ['" + red + k + "", end=(ENDC + "'] = '" + lightblue + v + ENDC + "'\n"))
