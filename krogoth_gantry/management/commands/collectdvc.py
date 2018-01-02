from django.core.management.base import BaseCommand
from krogoth_gantry.models import KrogothGantryMasterViewController, KrogothGantryIcon, KrogothGantryService, \
    KrogothGantryCategory, KrogothGantrySlaveViewController, KrogothGantryDirective, AKGantryMasterViewController
import codecs
import os
from scss import Compiler



from krogoth_gantry.management.commands.installdjangular import bcolors
import random
class Command(BaseCommand):
    help = 'prints the toolbar module and controller.'

    # def add_arguments(self, parser):
    #     parser.add_argument('mvc_id', nargs="+", type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(''))

        has_master = False

        all_old_ones = AKGantryMasterViewController.objects.all()
        for old in all_old_ones:
            old.delete()
        icon = KrogothGantryIcon()
        count_icons = len(KrogothGantryIcon.objects.all())
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

        log_last_path = ''
        gantry_catagories = os.listdir('krogoth_gantry/DVCManager')
        i = 0
        for gantry in gantry_catagories:
            i += 1
            if gantry[0] != '.' and gantry != 'MiscDVC':
                djangular_dvcs = os.listdir('krogoth_gantry/DVCManager/' + gantry)
                catagory = ''
                for dvc in djangular_dvcs:
                    if dvc[0] == '.':
                        continue
                    name_pk = dvc
                    dvc = gantry + '/' + dvc
                    has_slave = False
                    has_services = False
                    has_directives = False

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
                        style = '/**/'
                        title = 'Untitled'
                        subcatagory = ''
                        if os.path.exists('krogoth_gantry/DVCManager/' + dvc + '/Title.txt'):
                            title = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/Title.txt', 'r').read()
                        if os.path.exists('krogoth_gantry/DVCManager/' + dvc + '/SubCatagory.txt'):
                            subcatagory = '.' + codecs.open('krogoth_gantry/DVCManager/' + dvc + '/SubCatagory.txt',
                                                            'r').read()
                        if os.path.exists('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/style.css'):
                            style = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/style.css', 'r').read()

                        if os.path.exists('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/style.scss'):
                            rawcode = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/style.scss', 'r').read()
                            compiled = Compiler().compile_string(rawcode)
                            style += compiled

                        str_View = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/view.html', 'r').read()
                        str_Module = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/module.js', 'r').read()
                        str_Controller = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/controller.js',
                                                     'r').read()
                        _mvc = AKGantryMasterViewController.objects.get_or_create(name=name_pk + '_akdvc',
                                                                                       title=title, category=cat,
                                                                                       icon=icon)


                        # view_html=str_View,
                        # controller_js=str_Controller,
                        # module_js=str_Module,
                        # category=cat[0],
                        # icon=icon)


                        clean_catagory = catagory.replace(' ', '').replace('-', '')
                        set_catagory = str_Module.replace('AK_NAVCAT_KROGOTH', clean_catagory)
                        parsed_module = set_catagory.replace('.AK_SUBCATAGORY_KROGOTH', subcatagory)

                        _mvc[0].style_css = style
                        _mvc[0].view_html = str_View
                        _mvc[0].controller_js = str_Controller
                        _mvc[0].module_js = parsed_module.replace("msNavigationServiceProvider.saveItem('.",
                                                                  "msNavigationServiceProvider.saveItem('")
                        # _mvc[0].category=cat[0]
                        # _mvc[0].icon=icon[0]


                        if has_slave == True:
                            try:
                                KrogothGantrySlaveViewController.objects.get(name=name_pk + 'Slave').delete()
                                print('deleting old slave...')
                            except:
                                pass
                            svc = KrogothGantrySlaveViewController.objects.get_or_create(name=name_pk + 'Slave')
                            svc[0].title = name_pk + '_Slave' + str(i)
                            log_last_path = 'krogoth_gantry/DVCManager/' + dvc + '/MasterVC/view.html'
                            str_slaveV = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/view.html',
                                                     'r').read()
                            str_slaveC = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/controller.js',
                                                     'r').read()
                            svc[0].view_html = str_slaveV
                            svc[0].controller_js = str_slaveC
                            svc[0].save()
                            _mvc[0].djangular_slave_vc.add(svc[0])

                        if has_services == True:
                            srv_files = os.listdir('krogoth_gantry/DVCManager/' + dvc + '/Services')
                            for srv in srv_files:
                                if srv[0] != '.':  # ignore hidden OS files
                                    log_last_path = 'krogoth_gantry/DVCManager/' + dvc + '/Services/' + srv
                                    str_srv = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/Services/' + srv,
                                                          'r').read()
                                    try:
                                        KrogothGantryService.objects.get(name=srv[:-3]).delete()
                                        print('deleting old service...')
                                    except:
                                        pass
                                    service = KrogothGantryService.objects.get_or_create(name=srv[:-3])
                                    service[0].title = srv + '_Service'
                                    service[0].service_js = str_srv
                                    service[0].save()
                                    _mvc[0].djangular_service.add(service[0])

                        if has_directives == True:
                            drec_files = os.listdir('krogoth_gantry/DVCManager/' + dvc + '/Directives')
                            for drec in drec_files:
                                if drec[0] != '.':  # ignore hidden OS files
                                    log_last_path = 'krogoth_gantry/DVCManager/' + dvc + '/Directives/' + drec
                                    str_drec = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/Directives/' + drec,
                                                           'r').read()
                                    try:
                                        KrogothGantryDirective.objects.get(name=drec[:-3]).delete()
                                        print('deleting old directive...')
                                    except:
                                        pass
                                    directive = KrogothGantryDirective.objects.get_or_create(name=drec[:-3])
                                    directive[0].title = drec + '_Directive'
                                    directive[0].directive_js = str_drec
                                    directive[0].save()
                                    _mvc[0].djangular_directive.add(directive[0])

                        _mvc[0].icon = KrogothGantryIcon.objects.get(id=int(random.randint(i, count_icons - 20)))
                        _mvc[0].save()
                        self.stdout.write(self.style.SUCCESS('DVC Manager Saved: ' + dvc))
        # try:
        #
        # except Exception as ex:
        #     print(bcolors.red + 'Krogoth DVC Manager Failed, there might be a conflict. To resolve this, delete all Krogoth ', end='')
        #     print('Gantry objects from the database that were previously generated by this collectdvc command.', end='')
        #     print(bcolors.ENDC)
        #     print(ex)
        #     print(bcolors.orange + log_last_path + bcolors.ENDC)


