from django.core.management.base import BaseCommand, CommandError
from Djangular.models import DjangularMasterViewController, DjangularSlaveViewController, \
    DjangularService, DjangularDirective

# python3 manage.py print_djangularmastervc 1
# f = open('Djangular/management/default_templates/base_controller.js', 'r')
class Command(BaseCommand):
    help = 'prints the contents of a Djangular Master View Controllers, given the id of the dmvc as an argument'
    def add_arguments(self, parser):
        parser.add_argument('mvc_id', nargs="+", type=int)
    def handle(self, *args, **options):
        for mvc_id in options['mvc_id']:
            if mvc_id == -1:
                djangularApp = DjangularMasterViewController.objects.all()
                for app in djangularApp:
                    self.stdout.write("Saving Djangular Master View Controllers", ending='\n')

                    text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".module" + ".js", "w")
                    text_file.write(app.module_js)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(app.name + '_module'))
                    self.stdout.write(self.style.WARNING(
                        "Djangular/management/backups/" + app.name + str(app.id) + ".module" + ".js"))

                    text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".controller" + ".js", "w")
                    text_file.write(app.controller_js)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(app.name + '_controller'))
                    self.stdout.write(self.style.WARNING(
                        "Djangular/management/backups/" + app.name + str(app.id) + ".controller" + ".js"))

                    text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".view" + ".html", "w")
                    text_file.write(app.view_html)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(app.name + '_view'))
                    self.stdout.write(self.style.WARNING(
                        "Djangular/management/backups/" + app.name + str(app.id) + ".view" + ".html"))

                djangularSlaves = DjangularSlaveViewController.objects.all()
                for app in djangularSlaves:
                    self.stdout.write("Saving Djangular Slave View Controllers", ending='\n')
                    text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".controller" + ".js", "w")
                    text_file.write(app.controller_js)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(app.name + '_controller'))
                    self.stdout.write(self.style.WARNING(
                        "Djangular/management/backups/" + app.name + str(app.id) + ".controller" + ".js"))

                    text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".view" + ".html", "w")
                    text_file.write(app.view_html)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(app.name + '_view'))
                    self.stdout.write(self.style.WARNING(
                        "Djangular/management/backups/" + app.name + str(app.id) + ".view" + ".html"))

                djangularServices = DjangularService.objects.all()
                for app in djangularServices:
                    self.stdout.write("Saving Djangular Services", ending='\n')
                    text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".service" + ".js", "w")
                    text_file.write(app.service_js)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(app.name + '_service'))
                    self.stdout.write(self.style.WARNING(
                        "Djangular/management/backups/" + app.name + str(app.id) + ".service" + ".js"))

                djangularDirectives = DjangularDirective.objects.all()
                for app in djangularDirectives:
                    self.stdout.write("Saving Djangular Directives", ending='\n')
                    text_file = open("Djangular/management/backups/" + app.name + str(app.id) + ".directive" + ".js", "w")
                    text_file.write(app.directive_js)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(app.name + '_directive'))
                    self.stdout.write(self.style.WARNING(
                        "Djangular/management/backups/" + app.name + str(app.id) + ".directive" + ".js"))

            else:
                djangularApp = DjangularMasterViewController.objects.get(id=mvc_id)
                self.stdout.write("", ending='\n\n')
                self.stdout.write(self.style.SUCCESS(djangularApp.module_js))
                self.stdout.write(self.style.SUCCESS(djangularApp.controller_js))
                self.stdout.write(self.style.SUCCESS(djangularApp.view_html))
