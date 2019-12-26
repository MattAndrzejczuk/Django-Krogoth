import os

from django.core.management.base import BaseCommand
from krogoth_gantry.helpers.kolors import ink
from krogoth_gantry.helpers.stores.filesystem_to_db import SaveMasterModuleJS, SaveMasterCtrlJS, SaveMasterViewHTML, \
    SaveDirectiveJS, SaveServiceJS

class Command(BaseCommand):
    help = 'prints the information about environment variables i.e. Redis host address, SQL password, etc...'
    
    def add_arguments(self, parser):
        parser.add_argument('--path', nargs="+", type=str)
        parser.add_argument('--name', nargs="+", type=str)
        parser.add_argument('--kind', nargs="+", type=str)
        parser.add_argument('--info', nargs="+", type=str)
        parser.add_argument('--examples', nargs="+", type=str)
    # print(options["mvc_id"][0])
    def handle(self, *args, **options):
        if options["info"] is not None:
            ink.pbluelight('--path ')
            ink.pgreen('path to file i.e. "static/web/app/Primary/Required/home/" \n')
            ink.pbluelight('--name ')
            ink.pgreen('unique database name i.e. "home" \n')
            ink.pbluelight('--kind ')
            ink.pgreen('file kinds: "controller", "module", "view", "directive", "service" \n')
        elif options["examples"] is not None:
            n1 = 'home'
            k1 = 'view'
            s1 = 'static/web/app/Primary/Required/'+n1+'/MasterVC/'+k1+'.html'
            ink.pred('\nEXAMPLES: \n')
            ink.pgreen('\n ./manage.py pushup --path "'+s1+'" --name "'+n1+'" --kind '+k1+' \n')
            n2 = 'home'
            k2 = 'controller'
            s2 = 'static/web/app/Primary/Required/' + n2 + '/MasterVC/' + k2 + '.html'
            ink.pgreen('\n ./manage.py pushup --path "' + s2 + '" --name "' + n2 + '" --kind ' + k2 + ' \n')
            n3 = 'Element_With_Events'
            k3 = 'directive'
            s3 = 'static/web/app/Directive_Examples/Another_Subcat/' + n3 + '/Directives/movieForm.js'
            ink.pgreen('\n ./manage.py pushup --path "' + s3 + '" --name "movieForm" --kind ' + k3 + ' \n')
            n4 = 'RESTfulModelI'
            k4 = 'service'
            s4 = 'static/web/app/Directive_Examples/RESTful_Samples/' + n4 + '/Services/RESTfulModelI.js'
            ink.pgreen('\n ./manage.py pushup --path "' + s4 + '" --name "' + n4 + '" --kind ' + k4 + ' \n')
        else:
            ink.pgreen("\n options ")
            ink.pred(" '--path'")
            path = options["path"][0]
            ink.pblue(path)
            ink.pred(" '--name'")
            name = options["name"][0]
            ink.pblue(name)
            ink.pred(" '--kind'")
            kind = options["kind"][0]
            ink.pblue(kind)
            if kind == 'controller':
                SaveMasterCtrlJS(name=name, path=path)
            elif kind == 'module':
                SaveMasterModuleJS(name=name, path=path)
            elif kind == 'view':
                SaveMasterViewHTML(name=name, path=path)
            elif kind == 'directive':
                SaveDirectiveJS(name=name, path=path)
            elif kind == 'service':
                SaveServiceJS(name=name, path=path)
        print()
