from django.core.management.base import BaseCommand
from krogoth_gantry.models.gantry_models import KrogothGantryMasterViewController
from krogoth_gantry.models.moho_extractor_models import IncludedHtmlMaster, IncludedHtmlCoreTemplate, IncludedJsMaster
from krogoth_core.models import AKFoundationAbstract

from krogoth_gantry.models.krogoth_manager import UncommitedSQL

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

                no_errors = True

                try:
                    p1 = static_root + "MasterVC/module.js"
                    text_file = open(p1, "w")
                    text_file.write(app.module_js)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(p1))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(p1))
                    UncommitedSQL.report_failure(for_record_named=app.name, error_info=(str(e)) + " MasterModule")
                    no_errors = False
                try:
                    p2 = static_root + "MasterVC/controller.js"
                    text_file = open(p2, "w")
                    text_file.write(app.controller_js)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(p2))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(p2))
                    UncommitedSQL.report_failure(for_record_named=app.name, error_info=(str(e)) + " MasterController")
                    no_errors = False
                try:
                    p3 = static_root + "MasterVC/view.html"
                    text_file = open(p3, "w")
                    text_file.write(app.view_html)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(p3))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(p3))
                    UncommitedSQL.report_failure(for_record_named=app.name, error_info=(str(e)) + " MasterView")
                    no_errors = False
                try:
                    p4 = static_root + "MasterVC/style.css"
                    text_file = open(p4, "w")
                    text_file.write(app.style_css)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(p4))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(p4))
                    UncommitedSQL.report_failure(for_record_named=app.name, error_info=(str(e)) + " StyleCSS")
                    no_errors = False
                try:
                    p5 = static_root + "MasterVC/themestyle.css"
                    text_file = open(p5, "w")
                    text_file.write(app.themestyle)
                    text_file.close()
                    self.stdout.write(self.style.SUCCESS(p5))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(p5))
                    UncommitedSQL.report_failure(for_record_named=app.name, error_info=(str(e)) + " ThemeStyleCSS")
                    no_errors = False
                if no_errors is True:
                    self.stdout.write(self.style.SUCCESS("No Errors Detected for MVC"))
                    UncommitedSQL.finish_and_remove(name=app.name)

            slave = app.djangular_slave_vc.all().first()
            try:
                if os.path.isfile(static_root + "SlaveVC/view.html"):
                    if UncommitedSQL.does_exist(name=slave.name, krogoth_class="KrogothGantrySlaveViewController"):
                        p4 = static_root + "SlaveVC/view.html"
                        text_file = open(p4, "w")
                        text_file.write(slave.view_html)
                        text_file.close()
                        self.stdout.write(self.style.SUCCESS(p4))
                        UncommitedSQL.finish_and_remove(name=slave.name)

                if os.path.isfile(static_root + "SlaveVC/controller.js"):
                    if UncommitedSQL.does_exist(name=slave.name, krogoth_class="KrogothGantrySlaveViewController"):
                        p5 = static_root + "SlaveVC/controller.js"
                        text_file = open(p5, "w")
                        text_file.write(slave.controller_js)
                        text_file.close()
                        self.stdout.write(self.style.SUCCESS(p5))
                        UncommitedSQL.finish_and_remove(name=slave.name)
            except Exception as e:
                self.stdout.write(self.style.ERROR("SLAVE FAILED TO SAVE TO FILESYSTEM"))
                UncommitedSQL.report_failure(for_record_named=slave.name, error_info=(str(e)) + " Slave")
### - - - - - - - - - - - - - UPDATE THE ERROR MESSAGES:
            djangularServices = app.djangular_service.all()
            for srv in djangularServices:
                if UncommitedSQL.does_exist(name=srv.name, krogoth_class="KrogothGantryService"):
                    try:

                        basedir = os.path.dirname(static_root + "Services/")
                        if not os.path.exists(basedir):
                            os.makedirs(basedir)
                        s1 = static_root + "Services/" + srv.name + ".js"
                        text_file = open(s1, "w")
                        text_file.write(srv.service_js)
                        text_file.close()
                        self.stdout.write(self.style.SUCCESS(s1))
                        UncommitedSQL.finish_and_remove(name=srv.name)
                    except Exception as e:
                        self.stdout.write(self.style.ERROR("Services FAILED TO SAVE TO FILESYSTEM"))
                        UncommitedSQL.report_failure(for_record_named=srv.name, error_info=(str(e)) + " Services")

            djangularDirectives = app.djangular_directive.all()
            for dtv in djangularDirectives:
                if UncommitedSQL.does_exist(name=dtv.name, krogoth_class="KrogothGantryDirective"):
                    try:
                        basedir = os.path.dirname(static_root + "Directives/")
                        if not os.path.exists(basedir):
                            os.makedirs(basedir)
                        d1 = static_root + "Directives/" + dtv.name + ".js"
                        text_file = open(d1, "w")
                        text_file.write(dtv.directive_js)
                        text_file.close()
                        self.stdout.write(self.style.SUCCESS(d1))
                        UncommitedSQL.finish_and_remove(name=dtv.name)
                    except Exception as e:
                        self.stdout.write(self.style.ERROR("Directives FAILED TO SAVE TO FILESYSTEM"))
                        UncommitedSQL.report_failure(for_record_named=dtv.name, error_info=(str(e)) + " Directives")


            tmplsHTML = IncludedHtmlMaster.objects.filter(master_vc=app.id)
            for tmpl in tmplsHTML:
                if UncommitedSQL.does_exist(name=tmpl.name, krogoth_class="IncludedHtmlMaster"):
                    try:
                        basedir = os.path.dirname(static_root + "partialsHTML/")
                        if not os.path.exists(basedir):
                            os.makedirs(basedir)
                        d1 = static_root + "partialsHTML/" + tmpl.name + ".html"
                        text_file = open(d1, "w")
                        text_file.write(tmpl.contents)
                        text_file.close()
                        self.stdout.write(self.style.SUCCESS(d1))
                        UncommitedSQL.finish_and_remove(name=tmpl.name)
                    except Exception as e:
                        self.stdout.write(self.style.ERROR("IncludedHtmlMaster FAILED TO SAVE TO FILESYSTEM"))
                        UncommitedSQL.report_failure(for_record_named=tmpl.name, error_info=(str(e)) + " IncludedHtmlMaster")

            tmplsJS = IncludedJsMaster.objects.filter(master_vc=app.id)
            for tmpl in tmplsJS:
                if UncommitedSQL.does_exist(name=tmpl.name, krogoth_class="IncludedJsMaster"):
                    try:
                        basedir = os.path.dirname(static_root + "partialsJS/")
                        if not os.path.exists(basedir):
                            os.makedirs(basedir)
                        d1 = static_root + "partialsJS/" + tmpl.name 
                        text_file = open(d1, "w")
                        text_file.write(tmpl.contents)
                        text_file.close()
                        self.stdout.write(self.style.SUCCESS(d1))
                        UncommitedSQL.finish_and_remove(name=tmpl.name)
                    except Exception as e:
                        self.stdout.write(self.style.ERROR("IncludedJsMaster FAILED TO SAVE TO FILESYSTEM"))
                        UncommitedSQL.report_failure(for_record_named=tmpl.name,
                                                     error_info=(str(e)) + " IncludedJsMaster")

            coreJSFiles = AKFoundationAbstract.objects.all()
            for fuse in coreJSFiles:
                try:
                    if UncommitedSQL.does_exist(name=fuse.unique_name, krogoth_class="AKFoundation"):
                        d1 = fuse.path + fuse.first_name + "." + fuse.last_name + fuse.ext
                        text_file = open(d1, "w")
                        text_file.write(fuse.code)
                        text_file.close()
                        self.stdout.write(self.style.SUCCESS(d1))
                        UncommitedSQL.finish_and_remove(name=fuse.unique_name)
                except Exception as e:
                    self.stdout.write(self.style.ERROR("AKFoundation FAILED TO SAVE TO FILESYSTEM"))
                    UncommitedSQL.report_failure(for_record_named=fuse.unique_name,
                                                 error_info=(str(e)) + " AKFoundation")

            coreHTMLs = IncludedHtmlCoreTemplate.objects.all()
            for html in coreHTMLs:
                if UncommitedSQL.does_exist(name=html.name, krogoth_class="NgIncludedHtmlCore"):
                    try:
                        filep = html.os_path + html.file_name
                        sys_file = open(filep, "w")
                        sys_file.write(html.contents)
                        sys_file.close()
                        print(html.name)
                        self.stdout.write(self.style.SUCCESS(filep))
                        UncommitedSQL.finish_and_remove(name=html.name)
                    except Exception as e:
                        self.stdout.write(self.style.ERROR("NgIncludedHtmlCore FAILED TO SAVE TO FILESYSTEM"))
                        UncommitedSQL.report_failure(for_record_named=html.unique_name,
                                                     error_info=(str(e)) + " NgIncludedHtmlCore")
