from django.core.management.base import BaseCommand, CommandError
from krogoth_gantry.models import KrogothGantryMasterViewController
from moho_extractor.models import IncludedHtmlMaster, IncludedHtmlCoreTemplate
from krogoth_core.models import AKFoundationAbstract

from krogoth_admin.models import UncommitedSQL

import os


# python3 manage.py backupdjangular

class Command(BaseCommand):
    help = 'Backup all js and html angular code that lives in SQL'

    def handle(self, *args, **options):
        djangularApp = KrogothGantryMasterViewController.objects.all()
        for app in djangularApp:
            static_root = app.path_to_static
            # self.stdout.write("Saving krogoth_gantry Master View Controllers", ending='\n')
            if UncommitedSQL.does_exist(name=app.name, krogoth_class="KrogothGantryMasterViewController") == True:
                UncommitedSQL.finish_and_remove(name=app.name)

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
                p4 = static_root + "MasterVC/style.css"
                text_file = open(p4, "w")
                text_file.write(app.style_css)
                text_file.close()
                self.stdout.write(self.style.SUCCESS(p4))
                p5 = static_root + "MasterVC/themestyle.css"
                text_file = open(p5, "w")
                text_file.write(app.themestyle)
                text_file.close()
                self.stdout.write(self.style.SUCCESS(p5))

            slave = app.djangular_slave_vc.all().first()
            if os.path.isfile(static_root + "SlaveVC/view.html"):
                if UncommitedSQL.does_exist(name=slave.name, krogoth_class="KrogothGantrySlaveViewController"):
                    UncommitedSQL.finish_and_remove(name=slave.name)
                    p4 = static_root + "SlaveVC/view.html"
                    text_file = open(p4, "w")
                    text_file.write(slave.view_html)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(p4))
            if os.path.isfile(static_root + "SlaveVC/controller.js"):
                if UncommitedSQL.does_exist(name=slave.name, krogoth_class="KrogothGantrySlaveViewController"):
                    UncommitedSQL.finish_and_remove(name=slave.name)
                    p5 = static_root + "SlaveVC/controller.js"
                    text_file = open(p5, "w")
                    text_file.write(slave.controller_js)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(p5))
            djangularServices = app.djangular_service.all()
            for srv in djangularServices:
                if UncommitedSQL.does_exist(name=srv.name, krogoth_class="KrogothGantryService"):
                    UncommitedSQL.finish_and_remove(name=srv.name)
                    basedir = os.path.dirname(static_root + "Services/")
                    if not os.path.exists(basedir):
                        os.makedirs(basedir)
                    s1 = static_root + "Services/" + srv.name + ".js"
                    text_file = open(s1, "w")
                    text_file.write(srv.service_js)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(s1))
            djangularDirectives = app.djangular_directive.all()
            for dtv in djangularDirectives:
                if UncommitedSQL.does_exist(name=dtv.name, krogoth_class="KrogothGantryDirective"):
                    UncommitedSQL.finish_and_remove(name=dtv.name)
                    basedir = os.path.dirname(static_root + "Directives/")
                    if not os.path.exists(basedir):
                        os.makedirs(basedir)
                    d1 = static_root + "Directives/" + dtv.name + ".js"
                    text_file = open(d1, "w")
                    text_file.write(dtv.directive_js)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(d1))
            tmplsHTML = IncludedHtmlMaster.objects.filter(master_vc=app.id)
            for tmpl in tmplsHTML:
                if UncommitedSQL.does_exist(name=tmpl.name, krogoth_class="IncludedHtmlMaster"):
                    UncommitedSQL.finish_and_remove(name=tmpl.name)
                    basedir = os.path.dirname(static_root + "partialsHTML/")
                    if not os.path.exists(basedir):
                        os.makedirs(basedir)
                    d1 = static_root + "partialsHTML/" + tmpl.name + ".html"
                    text_file = open(d1, "w")
                    text_file.write(tmpl.contents)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(d1))
            coreJSFiles = AKFoundationAbstract.objects.all()
            for fuse in coreJSFiles:
                if UncommitedSQL.does_exist(name=fuse.unique_name, krogoth_class="AKFoundation"):
                    UncommitedSQL.finish_and_remove(name=fuse.unique_name)
                    # basedir = os.path.dirname(static_root + "partialsHTML/")
                    # if not os.path.exists(basedir):
                    #    os.makedirs(basedir)
                    d1 = fuse.path + fuse.first_name + "." + fuse.last_name + fuse.ext
                    text_file = open(d1, "w")
                    text_file.write(fuse.code)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(d1))