from django.core.management.base import BaseCommand, CommandError
from krogoth_gantry.models import KrogothGantryMasterViewController, KrogothGantrySlaveViewController, \
    KrogothGantryService, KrogothGantryDirective

# python3 manage.py backupdjangular

class Command(BaseCommand):
    help = 'Backup all js and html angular code that lives in SQL'

    def handle(self, *args, **options):
        djangularApp = KrogothGantryMasterViewController.objects.all()
        for app in djangularApp:
            # self.stdout.write("Saving krogoth_gantry Master View Controllers", ending='\n')

            text_file = open("krogoth_gantry/management/backups/" + app.name + str(app.id) + ".module" + ".js", "w")
            text_file.write(app.module_js)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_module'))
            self.stdout.write(self.style.WARNING(
                "krogoth_gantry/management/backups/" + app.name + str(app.id) + ".module" + ".js"))

            text_file = open("krogoth_gantry/management/backups/" + app.name + str(app.id) + ".controller" + ".js", "w")
            text_file.write(app.controller_js)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_controller'))
            self.stdout.write(self.style.WARNING(
                "krogoth_gantry/management/backups/" + app.name + str(app.id) + ".controller" + ".js"))

            text_file = open("krogoth_gantry/management/backups/" + app.name + str(app.id) + ".view" + ".html", "w")
            text_file.write(app.view_html)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_view'))
            self.stdout.write(self.style.WARNING(
                "krogoth_gantry/management/backups/" + app.name + str(app.id) + ".view" + ".html"))

        djangularSlaves = KrogothGantrySlaveViewController.objects.all()
        for app in djangularSlaves:
            # self.stdout.write("Saving krogoth_gantry Slave View Controllers", ending='\n')
            text_file = open("krogoth_gantry/management/backups/" + app.name + str(app.id) + ".controller" + ".js", "w")
            text_file.write(app.controller_js)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_controller'))
            self.stdout.write(self.style.WARNING(
                "krogoth_gantry/management/backups/" + app.name + str(app.id) + ".controller" + ".js"))

            text_file = open("krogoth_gantry/management/backups/" + app.name + str(app.id) + ".view" + ".html", "w")
            text_file.write(app.view_html)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_view'))
            self.stdout.write(self.style.WARNING(
                "krogoth_gantry/management/backups/" + app.name + str(app.id) + ".view" + ".html"))

        djangularServices = KrogothGantryService.objects.all()
        for app in djangularServices:
            # self.stdout.write("Saving krogoth_gantry Services", ending='\n')
            text_file = open("krogoth_gantry/management/backups/" + app.name + str(app.id) + ".service" + ".js", "w")
            text_file.write(app.service_js)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_service'))
            self.stdout.write(self.style.WARNING(
                "krogoth_gantry/management/backups/" + app.name + str(app.id) + ".service" + ".js"))

        djangularDirectives = KrogothGantryDirective.objects.all()
        for app in djangularDirectives:
            # self.stdout.write("Saving krogoth_gantry Directives", ending='\n')
            text_file = open("krogoth_gantry/management/backups/" + app.name + str(app.id) + ".directive" + ".js", "w")
            text_file.write(app.directive_js)
            text_file.close()
            # self.stdout.write(self.style.SUCCESS(app.name + '_directive'))
            self.stdout.write(self.style.WARNING(
                "krogoth_gantry/management/backups/" + app.name + str(app.id) + ".directive" + ".js"))