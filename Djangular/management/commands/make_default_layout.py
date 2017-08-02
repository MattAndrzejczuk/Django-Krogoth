from django.core.management.base import BaseCommand, CommandError
from Djangular.models import DjangularMasterViewController





#  READ JS & HTML FILES AS A STRING LIKE SO:

#     f = open('Djangular/management/default_templates/base_controller.js', 'r')



class Command(BaseCommand):
    help = 'prints the contents of a Djangular Master View Controllers, given the id of the dmvc as an argument'

    def add_arguments(self, parser):
        parser.add_argument('mvc_id', nargs="+", type=int)

    def handle(self, *args, **options):
        for mvc_id in options['mvc_id']:
            djangularApp = DjangularMasterViewController.objects.get(id=mvc_id)

            self.stdout.write("", ending='\n\n')
            self.stdout.write(self.style.SUCCESS(djangularApp.module_js))
            self.stdout.write(self.style.SUCCESS(djangularApp.controller_js))
            self.stdout.write(self.style.SUCCESS(djangularApp.view_html))
