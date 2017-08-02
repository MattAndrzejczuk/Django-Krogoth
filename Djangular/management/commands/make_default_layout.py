from django.core.management.base import BaseCommand, CommandError
from Djangular.models import DjangularMasterViewController


#  READ JS & HTML FILES AS A STRING LIKE SO:
#     f = open('static/app/toolbar/toolbar.controller.js', 'r')
#     f = open('static/app/toolbar/toolbar.module.js', 'r')










class Command(BaseCommand):
    help = 'prints the toolbar module and controller.'

    # def add_arguments(self, parser):
    #     parser.add_argument('mvc_id', nargs="+", type=int)

    def handle(self, *args, **options):
        ctrl = open('static/app/toolbar/toolbar.controller.js', 'r')
        module = open('static/app/toolbar/toolbar.module.js', 'r')

        str_ctrl = ctrl.read()
        str_module = module.read()

        self.stdout.write("", ending='\n\n')
        self.stdout.write(self.style.SUCCESS( str_ctrl ))
        self.stdout.write("", ending='\n\n')
        self.stdout.write(self.style.SUCCESS( str_module ))



