
from django.core.management.base import BaseCommand


from Djangular.models import DjangularMasterViewController, DjangularIcon, DjangularService, \
    DjangularCategory, DjangularSlaveViewController, DjangularDirective
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

        icon = DjangularIcon()
        try:
            icon = DjangularIcon(name='s16 icon-ta-arm', code='s16 icon-ta-arm')
            icon.save()
        except:
            icon = DjangularIcon.objects.get(name='s16 icon-ta-arm')


        cat = DjangularCategory.objects.get_or_create(name='DVC')


        djangular_dvcs = os.listdir('Djangular/DVCManager')
        for dvc in djangular_dvcs:
            components = os.listdir('Djangular/DVCManager/' + dvc)
            serv_path = 'Djangular/DVCManager/' + dvc + '/Services'
            if os.path.isdir(serv_path):
                if len(os.listdir(serv_path)) >= 1:
                    has_services = True
            direc_path = 'Djangular/DVCManager/' + dvc + '/Directives'
            if os.path.isdir(direc_path):
                if len(os.listdir(direc_path)) >= 1:
                    has_directives = True
            slave_path = 'Djangular/DVCManager/' + dvc + '/SlaveVC'
            if os.path.isdir(slave_path):
                if len(os.listdir(slave_path)) >= 1:
                    has_slave = True
            master_path = 'Djangular/DVCManager/' + dvc + '/MasterVC'
            if os.path.isdir(master_path):
                if len(os.listdir(master_path)) >= 1:
                    has_master = True

            if has_master == True:
                title = 'Untitled'
                if os.path.exists('Djangular/DVCManager/' + dvc + '/Title.txt'):
                    title = codecs.open('Djangular/DVCManager/' + dvc + '/Title.txt', 'r').read()
                str_View = codecs.open('Djangular/DVCManager/' + dvc + '/MasterVC/view.html', 'r').read()
                str_Module = codecs.open('Djangular/DVCManager/' + dvc + '/MasterVC/module.js', 'r').read()
                str_Controller = codecs.open('Djangular/DVCManager/' + dvc + '/MasterVC/controller.js', 'r').read()
                _mvc = DjangularMasterViewController.objects.get_or_create(name=dvc, title=title, view_html=str_View, controller_js=str_Controller, module_js=str_Module, category=cat[0], icon=icon)
                mvc = DjangularMasterViewController.objects.get(id=_mvc[0].id)

                svc = DjangularSlaveViewController.objects.get_or_create(name=dvc+'slave')
                svc[0].title = 'Thread'
                if has_slave == True:
                    str_slaveV = codecs.open('Djangular/DVCManager/' + dvc + '/MasterVC/view.html','r').read()
                    str_slaveC = codecs.open('Djangular/DVCManager/' + dvc + '/MasterVC/controller.js','r').read()
                    svc[0].view_html = str_slaveV
                    svc[0].controller_js = str_slaveC
                    svc[0].save()
                    mvc.djangular_slave_vc.add(svc[0])

                if has_services == True:
                    srv_files = os.listdir('Djangular/DVCManager/' + dvc + '/Services')
                    for srv in srv_files:
                        str_srv = codecs.open('Djangular/DVCManager/' + dvc + '/Services/' + srv,'r').read()
                        service = DjangularService.objects.get_or_create(name=srv[:-3])
                        service[0].title = srv + ' Service'
                        service[0].service_js = str_srv
                        service[0].save()
                        mvc.djangular_service.add(service[0])

                if has_directives == True:
                    drec_files = os.listdir('Djangular/DVCManager/' + dvc + '/Directives')
                    for drec in drec_files:
                        str_drec = codecs.open('Djangular/DVCManager/' + dvc + '/Directives/' + drec, 'r').read()
                        directive = DjangularDirective.objects.get_or_create(name=drec[:-3])
                        directive[0].title = drec + ' Directive'
                        directive[0].directive_js = str_drec
                        directive[0].save()
                        mvc.djangular_directive.add(directive[0])

                mvc.icon = icon
                mvc.save()
                self.stdout.write(self.style.SUCCESS('DVC Manager Saved: ' + dvc))
