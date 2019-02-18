from django.core.management.base import BaseCommand
from krogoth_gantry.models import KrogothGantryService, \
    KrogothGantryCategory, KrogothGantrySlaveViewController, KrogothGantryDirective, AKGantryMasterViewController
import codecs
import os
from scss import Compiler
import json
from moho_extractor.models import IncludedHtmlMaster, IncludedJsMaster


class Command(BaseCommand):
    help = 'prints the toolbar module and controller.'

    # def add_arguments(self, parser):
    #     parser.add_argument('mvc_id', nargs="+", type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(''))

        has_master = False

        oldCatagories = KrogothGantryCategory.objects.all()
        all_old_ones = AKGantryMasterViewController.objects.all()
        for old in all_old_ones:
            old.delete()
        for old in oldCatagories:
            old.delete()


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
                cat_host_obj = cat
                cats_exist = KrogothGantryCategory.objects.filter(name=gantry)
                if len(cats_exist) < 1:
                    cat_host_obj = KrogothGantryCategory(name=gantry.replace(' ','_'),
                                                         title=gantry.replace('_',' '))
                    cat_host_obj.save()

                krogoth_subcats = os.listdir('krogoth_gantry/DVCManager/' + gantry)
                for subcats in krogoth_subcats:
                    if subcats[0] == '.':
                        continue
                    elif subcats[-4:].lower() == 'json':
                        with open('krogoth_gantry/DVCManager/' + gantry + '/' + subcats) as json_data:
                            d = json.load(json_data)
                            cat_host_obj.weight = d['weight']
                            cat_host_obj.save()
                        continue
                    cat_sub_obj = cat
                    cats_exist = KrogothGantryCategory.objects.filter(name=subcats)
                    if len(cats_exist) < 1:
                        cat_sub_obj = KrogothGantryCategory(name=subcats.replace(' ', '_'),
                                                            title=subcats.replace('_', ' '),
                                                            parent=cat_host_obj)
                        cat_sub_obj.save()

                    djangular_dvcs = os.listdir('krogoth_gantry/DVCManager/' + gantry + '/' + subcats)
                    num_weight = 5
                    for dvc in djangular_dvcs:
                        if dvc[0] == '.':
                            continue
                        elif dvc[-4:].lower() == 'json':
                            with open('krogoth_gantry/DVCManager/' + gantry + '/' + subcats + '/' + dvc) as json_data:
                                d = json.load(json_data)
                                cat_sub_obj.weight = d['weight']
                                try:
                                    num_weight = d["weight"]
                                except: pass;
                                cat_sub_obj.save()
                            continue
                        name_pk = dvc
                        dvc = gantry + '/' + subcats + '/' + dvc
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
                            # subcatagory = ''


                            not_lazy = True
                            _AKLazyTxt = 'krogoth_gantry/DVCManager/' + dvc + '/LAZY.txt'
                            if os.path.isfile(_AKLazyTxt):
                                print("LAZY CREATING....")
                                print('krogoth_gantry/DVCManager/' + dvc + '/LAZY.txt')
                                not_lazy = False
                            _AKTitleTxt = 'krogoth_gantry/DVCManager/' + dvc + '/Title.txt'
                            if os.path.exists(_AKTitleTxt):
                                title = codecs.open(_AKTitleTxt, 'r').read()
                            _AKStyleCSSMVC = 'krogoth_gantry/DVCManager/' + dvc + '/MasterVC/style.css'
                            if os.path.exists(_AKStyleCSSMVC):
                                style = codecs.open(_AKStyleCSSMVC, 'r').read()
                            if os.path.exists('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/style.scss'):
                                rawcode = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/MasterVC/style.scss',
                                                      'r').read()
                                compiled = Compiler().compile_string(rawcode)
                                style += compiled

                            _AKStyleModuleMVC = 'krogoth_gantry/DVCManager/' + dvc + '/MasterVC/module.js'
                            _AKStyleCtrlMVC = 'krogoth_gantry/DVCManager/' + dvc + '/MasterVC/controller.js'
                            _AKStyleViewMVC = 'krogoth_gantry/DVCManager/' + dvc + '/MasterVC/view.html'
                            str_View = codecs.open(_AKStyleViewMVC, 'r').read()
                            str_Module = codecs.open(_AKStyleModuleMVC, 'r').read()
                            str_Controller = codecs.open(_AKStyleCtrlMVC,
                                                         'r').read()
                            _mvc = AKGantryMasterViewController.objects.get_or_create(name=name_pk,
                                                                                      title=title, category=cat_sub_obj,
                                                                                      is_enabled=not_lazy)

                            partial_HTMLs_path = 'krogoth_gantry/DVCManager/' + dvc + '/partialsHTML'
                            if os.path.isdir(partial_HTMLs_path):
                                htmls = os.listdir(partial_HTMLs_path)
                                if len(os.listdir(partial_HTMLs_path)) >= 1:
                                    for html in htmls:
                                        if html == ".DS_Store":
                                            continue
                                        rawHtml = ""
                                        pathHTML = partial_HTMLs_path + "/" + html
                                        try:
                                            rawHtml = codecs.open(pathHTML, 'r').read()
                                            self.stdout.write(self.style.SUCCESS(" ✅  Successfully loaded file: " + pathHTML))
                                        except:
                                            rawHtml = ""
                                            self.stdout.write(self.style.ERROR("Skipping file: " + pathHTML))
                                        html_name = html
                                        if html[-5:].lower() == ".html":
                                            html_name = html[:-5]
                                        newIncludeHTML = IncludedHtmlMaster.objects.get_or_create(
                                            name=(html_name),
                                            master_vc=_mvc[0])
                                        newIncludeHTML[0].sys_path = pathHTML
                                        newIncludeHTML[0].contents = rawHtml
                                        newIncludeHTML[0].save()
                                        print("TOTAL PARTIALS: " + str(len(IncludedHtmlMaster.objects.all())))

                            partial_JSs_path = 'krogoth_gantry/DVCManager/' + dvc + '/partialsJS'
                            if os.path.isdir(partial_JSs_path):
                                jss = os.listdir(partial_JSs_path)
                                if len(os.listdir(partial_JSs_path)) >= 1:
                                    for js in jss:
                                        if js == ".DS_Store":
                                            continue
                                        rawJs = ""
                                        pathJS = partial_JSs_path + "/" + js
                                        try:
                                            rawJs = codecs.open(pathJS, 'r').read()
                                            self.stdout.write(self.style.SUCCESS(" ✅  Successfully loaded file: " + pathJS))
                                        except:
                                            rawJs = ""
                                            self.stdout.write(self.style.ERROR("Skipping file: " + pathJS))
                                        js_name = js
                                        if js[-5:].lower() == ".js":
                                            js_name = js[:-5]
                                        newIncludeJS = IncludedJsMaster.objects.get_or_create(
                                            name=(js_name),
                                            master_vc=_mvc[0])
                                        newIncludeJS[0].sys_path = pathJS
                                        newIncludeJS[0].contents = rawJs
                                        newIncludeJS[0].save()
                                        print("TOTAL PARTIALS: " + str(len(IncludedJsMaster.objects.all())))

                            # clean_catagory = catagory.replace(' ', '').replace('-', '')
                            # clean_subcatagory = subcatagory.replace(' ', '').replace('-', '')
                            _mvc[0].path_to_static = 'krogoth_gantry/DVCManager/' + dvc + '/'
                            _mvc[0].style_css = style
                            _mvc[0].view_html = str_View
                            _mvc[0].controller_js = str_Controller
                            _mvc[0].module_js = str_Module.replace("msNavigationServiceProvider.saveItem('.",
                                                                   "msNavigationServiceProvider.saveItem('").replace('"AK_GANTRY_WEIGHT"', str(num_weight))

                            if has_slave == True:
                                try:
                                    KrogothGantrySlaveViewController.objects.get(name=name_pk + 'Slave').delete()
                                    print('deleting old slave...')
                                except:
                                    pass
                                svc = KrogothGantrySlaveViewController.objects.get_or_create(name=name_pk + 'Slave')
                                svc[0].title = name_pk + '_Slave' + str(i)
                                log_last_path = 'krogoth_gantry/DVCManager/' + dvc + '/SlaveVC/view.html'
                                str_slaveV = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/SlaveVC/view.html',
                                                         'r').read()
                                str_slaveC = codecs.open('krogoth_gantry/DVCManager/' + dvc + '/SlaveVC/controller.js',
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
                                        service[0].title = srv[:-3]  # + '_Service'
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
                                        directive[0].title = drec[:-3]# + '_Directive'
                                        directive[0].directive_js = str_drec
                                        directive[0].save()
                                        _mvc[0].djangular_directive.add(directive[0])


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
