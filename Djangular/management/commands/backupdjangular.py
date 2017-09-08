from django.core.management.base import BaseCommand, CommandError
from Djangular.models import DjangularMasterViewController, DjangularSlaveViewController, \
    DjangularService, DjangularDirective

# python3 manage.py backupdjangular

class Command(BaseCommand):
    help = 'Backup all js and html angular code that lives in SQL'

    def handle(self, *args, **options):
        djangularApp = DjangularMasterViewController.objects.all()
        for app in djangularApp:
            # self.stdout.write("Saving Djangular Master View Controllers", ending='\n')

            text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".module" + ".js", "w")
            text_file.write(app.module_js)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_module'))
            self.stdout.write(self.style.WARNING(
                "Djangular/management/backups/" + app.name + str(app.id) + ".module" + ".js"))

            text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".controller" + ".js", "w")
            text_file.write(app.controller_js)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_controller'))
            self.stdout.write(self.style.WARNING(
                "Djangular/management/backups/" + app.name + str(app.id) + ".controller" + ".js"))

            text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".view" + ".html", "w")
            text_file.write(app.view_html)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_view'))
            self.stdout.write(self.style.WARNING(
                "Djangular/management/backups/" + app.name + str(app.id) + ".view" + ".html"))

        djangularSlaves = DjangularSlaveViewController.objects.all()
        for app in djangularSlaves:
            # self.stdout.write("Saving Djangular Slave View Controllers", ending='\n')
            text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".controller" + ".js", "w")
            text_file.write(app.controller_js)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_controller'))
            self.stdout.write(self.style.WARNING(
                "Djangular/management/backups/" + app.name + str(app.id) + ".controller" + ".js"))

            text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".view" + ".html", "w")
            text_file.write(app.view_html)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_view'))
            self.stdout.write(self.style.WARNING(
                "Djangular/management/backups/" + app.name + str(app.id) + ".view" + ".html"))

        djangularServices = DjangularService.objects.all()
        for app in djangularServices:
            # self.stdout.write("Saving Djangular Services", ending='\n')
            text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".service" + ".js", "w")
            text_file.write(app.service_js)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_service'))
            self.stdout.write(self.style.WARNING(
                "Djangular/management/backups/" + app.name + str(app.id) + ".service" + ".js"))

        djangularDirectives = DjangularDirective.objects.all()
        for app in djangularDirectives:
            # self.stdout.write("Saving Djangular Directives", ending='\n')
            text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".directive" + ".js", "w")
            text_file.write(app.directive_js)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_directive'))
            self.stdout.write(self.style.WARNING(
                "Djangular/management/backups/" + app.name + str(app.id) + ".directive" + ".js"))