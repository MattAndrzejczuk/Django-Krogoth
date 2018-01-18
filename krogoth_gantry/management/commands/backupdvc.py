from django.core.management.base import BaseCommand, CommandError
from krogoth_gantry.models import KrogothGantryMasterViewController, KrogothGantrySlaveViewController, \
    KrogothGantryService, KrogothGantryDirective
import os
# python3 manage.py backupdjangular

class Command(BaseCommand):
    help = 'Backup all js and html angular code that lives in SQL'

    def handle(self, *args, **options):
        djangularApp = KrogothGantryMasterViewController.objects.all()
        for app in djangularApp:
            # self.stdout.write("Saving krogoth_gantry Master View Controllers", ending='\n')
            static_root = app.path_to_static
            p1 = static_root + "MasterVC/module.js"
            text_file = open(p1, "w")
            text_file.write(app.module_js)
            text_file.close()
            self.stdout.write(self.style.SUCCESS(p1))
            p2 = static_root + "MasterVC/controller.js"
            text_file = open(p2, "w")
            text_file.write(app.controller_js)
            text_file.close()
            self.stdout.write(self.style.SUCCESS(p2))
            p3 = static_root + "MasterVC/view.html"
            text_file = open(p3, "w")
            text_file.write(app.view_html)
            text_file.close()
            self.stdout.write(self.style.SUCCESS(p3))
            if os.path.isfile(static_root + "SlaveVC/view.html"):
                p4 = static_root + "SlaveVC/view.html"
                text_file = open(p4, "w")
                text_file.write(app.view_html)
                text_file.close()
                self.stdout.write(self.style.SUCCESS(p4))
            if os.path.isfile(static_root + "SlaveVC/controller.js"):
                p5 = static_root + "SlaveVC/controller.js"
                text_file = open(p5, "w")
                text_file.write(app.controller_js)
                text_file.close()
                self.stdout.write(self.style.SUCCESS(p5))
            djangularServices = app.djangular_service.all()
            for srv in djangularServices:
                s1 = static_root + "Services/" + srv.name + ".js"
                text_file = open(s1, "w")
                text_file.write(srv.service_js)
                text_file.close()
                self.stdout.write(self.style.SUCCESS(s1))
            djangularDirectives = app.djangular_directive.all()
            for dtv in djangularDirectives:
                d1 = static_root + "Directives/" + dtv.name + ".js"
                text_file = open(d1, "w")
                text_file.write(dtv.directive_js)
                text_file.close()
                self.stdout.write(self.style.SUCCESS(d1))