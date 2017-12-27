from django.core.management.base import BaseCommand
from krogoth_gantry.models import KrogothGantryMasterViewController, KrogothGantryIcon, KrogothGantryService, \
    KrogothGantryCategory, KrogothGantrySlaveViewController, KrogothGantryDirective
import codecs
import os


class Command(BaseCommand):
    help = 'prints the toolbar module and controller.'

    # def add_arguments(self, parser):
    #     parser.add_argument('mvc_id', nargs="+", type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(''))

        has_master = False
        has_slave = False
        has_services = False
        has_directives = False

        icon = KrogothGantryIcon()
        try:
            icon = KrogothGantryIcon(code='s16 icon-ta-arm')
            icon.save()
        except:
            icon = KrogothGantryIcon.objects.get(code='s16 icon-ta-arm')


        cat = KrogothGantryCategory()
        try:
            cat = KrogothGantryCategory(name='DVCManager')
            cat.save()
        except:
            cat = KrogothGantryCategory.objects.get(name='DVCManager')

        djangular_dvcs = os.listdir('krogoth_gantry/DVCManager')
        for dvc in djangular_dvcs:
            if dvc == '.DS_Store':
                continue
            components = os.listdir('krogoth_gantry/DVCManager/' + dvc)
            serv_path = 'krogoth_gantry/DVCManager/' + dvc + '/Services'
            if os.path.isdir(serv_path):
                if len(os.listdir(serv_path)) >= 1:
                    has_services = True
            direc_path = 'krogoth_gantry/DVCManager/' + dvc + '/Directives'
            if os.path.isdir(direc_path):
                if len(os.listdir(direc_path)) >= 1:
                    has_directives = True
            slave_path = 'krogoth_gantry/DVCManager/' + dvc + '/SlaveVC'
            if os.path.isdir(slave_path):
                if len(os.listdir(slave_path)) >= 1:
                    has_slave = True
            master_path = 'krogoth_gantry/DVCManager/' + dvc + '/MasterVC'
            if os.path.isdir(master_path):
                if len(os.listdir(master_path)) >= 1:
                    has_master = True

            if has_master == True:
                title = 'Untitled'
                if os.path.exists('krogoth_gantry/DVCManager/' + dvc + '/Title.txt'):
                    title = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/Title.txt', 'r').read()
                str_View = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/view.html', 'r').read()
                str_Module = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/module.js', 'r').read()
                str_Controller = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/controller.js', 'r').read()
                _mvc = KrogothGantryMasterViewController.objects.get_or_create(name=dvc,
                                                                               title=title, category=cat, icon=icon)
                                                                               # view_html=str_View,
                                                                               # controller_js=str_Controller,
                                                                               # module_js=str_Module,
                                                                               # category=cat[0],
                                                                               # icon=icon)
                _mvc[0].view_html=str_View
                _mvc[0].controller_js=str_Controller
                _mvc[0].module_js=str_Module
                # _mvc[0].category=cat[0]
                # _mvc[0].icon=icon[0]

                svc = KrogothGantrySlaveViewController.objects.get_or_create(name=dvc+'Slave')
                svc[0].title = dvc+'_Slave'
                if has_slave == True:
                    str_slaveV = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/view.html','r').read()
                    str_slaveC = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/controller.js','r').read()
                    svc[0].view_html = str_slaveV
                    svc[0].controller_js = str_slaveC
                    svc[0].save()
                    _mvc[0].djangular_slave_vc.add(svc[0])

                if has_services == True:
                    srv_files = os.listdir('krogoth_gantry/DVCManager/' + dvc + '/Services')
                    for srv in srv_files:
                        str_srv = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/Services/' + srv,'r').read()
                        service = KrogothGantryService.objects.get_or_create(name=srv[:-3])
                        service[0].title = srv + '_Service'
                        service[0].service_js = str_srv
                        service[0].save()
                        _mvc[0].djangular_service.add(service[0])

                if has_directives == True:
                    drec_files = os.listdir('krogoth_gantry/DVCManager/' + dvc + '/Directives')
                    for drec in drec_files:
                        str_drec = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/Directives/' + drec, 'r').read()
                        directive = KrogothGantryDirective.objects.get_or_create(name=drec[:-3])
                        directive[0].title = drec + '_Directive'
                        directive[0].directive_js = str_drec
                        directive[0].save()
                        _mvc[0].djangular_directive.add(directive[0])

                _mvc[0].icon = icon
                _mvc[0].save()
                self.stdout.write(self.style.SUCCESS('DVC Manager Saved: ' + dvc))
