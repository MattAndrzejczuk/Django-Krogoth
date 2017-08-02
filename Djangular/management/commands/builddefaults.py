from django.core.management.base import BaseCommand, CommandError
from Djangular.models import DjangularMasterViewController





class Command(BaseCommand):
    help = 'prints all Djangular Master View Controllers to allow for backups'

    def add_arguments(self, parser):
        parser.add_argument('mvc_id', nargs="+", type="int")

    def handle(self, *args, **options):
        for mvc_id in options['mvc_id']:
            djangularApp = DjangularMasterViewController.objects.get(id=mvc_id)

            self.stdout.write(self.style.SUCCESS(djangularApp.controller_js))
            