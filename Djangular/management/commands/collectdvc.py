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
            icon = DjangularIcon(name='s16 icon-ta-arm', code='icon-ubuntu')
            icon.save()
        except:
            icon = DjangularIcon.objects.get(name='s16 icon-ta-arm')

        cat = DjangularCategory()
        try:
            cat = DjangularCategory(name='DVC', code='nan')
            cat.save()
        except:
            cat = DjangularCategory.objects.get(name='Administration')

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
                mvc = DjangularMasterViewController.objects.get_or_create(name=dvc)
                mvc.title = title
                mvc.view_html = str_View
                mvc.controller_js = str_Controller
                mvc.module_js = str_Module
                mvc.save()

                svc = DjangularSlaveViewController.objects.get_or_create(name='Thread')
                svc.title = 'Thread'
                if has_slave == True:
                    str_slaveV = codecs.open('Djangular/DVCManager/' + dvc + '/MasterVC/view.html','r').read()
                    str_slaveC = codecs.open('Djangular/DVCManager/' + dvc + '/MasterVC/controller.js','r').read()
                    svc.view_html = str_slaveV
                    svc.controller_js = str_slaveC
                    svc.save()
                    mvc.djangular_slave_vc.add(svc)

                if has_services == True:
                    srv_files = os.listdir('Djangular/DVCManager/' + dvc + '/Services')
                    for srv in srv_files:
                        str_srv = codecs.open('Djangular/DVCManager/' + dvc + '/Services/' + srv,'r').read()
                        service = DjangularService.objects.get_or_create(name=srv)
                        service.title = srv + ' Service'
                        service.service_js = str_srv
                        service.save()
                        mvc.djangular_service.add(service)

                if has_directives == True:
                    drec_files = os.listdir('Djangular/DVCManager/' + dvc + '/Directives')
                    for drec in drec_files:
                        str_drec = codecs.open('Djangular/DVCManager/' + dvc + '/Directives/' + drec, 'r').read()
                        directive = DjangularDirective.objects.get_or_create(name=srv)
                        directive.title = srv + ' Directive'
                        directive.directive_js = str_drec
                        directive.save()
                        mvc.djangular_directive.add(directive)

                mvc.category = cat
                mvc.icon = icon
                mvc.save()
                self.stdout.write(self.style.SUCCESS('DVC Manager Saved: ' + dvc))
