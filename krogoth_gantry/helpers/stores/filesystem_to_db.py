from krogoth_gantry.models.gantry_models import KrogothGantryMasterViewController, KrogothGantryDirective, \
    KrogothGantryService
import codecs


class SaveMasterViewHTML():

    def __init__(self, path: str, name: str):
        self.path = path
        self.content = codecs.open(path, 'r').read()
        mvc = KrogothGantryMasterViewController.objects.get(name=name)
        mvc.view_html = self.content
        mvc.save()


class SaveMasterCtrlJS():

    def __init__(self, path: str, name: str):
        self.path = path
        self.content = codecs.open(path, 'r').read()
        mvc = KrogothGantryMasterViewController.objects.get(name=name)
        mvc.controller_js = self.content
        mvc.save()


class SaveMasterModuleJS():

    def __init__(self, path: str, name: str):
        self.path = path
        self.content = codecs.open(path, 'r').read()
        _mvc = KrogothGantryMasterViewController.objects.get(name=name)
        _mvc.module_js = self.content
        _mvc.save()


class SaveDirectiveJS():

    def __init__(self, path: str, name: str):
        self.path = path
        self.content = codecs.open(path, 'r').read()
        dir = KrogothGantryDirective.objects.get(name=name)
        dir.directive_js = self.content
        dir.save()


class SaveServiceJS():

    def __init__(self, path: str, name: str):
        self.path = path
        self.content = codecs.open(path, 'r').read()
        srv = KrogothGantryService.objects.get(name=name)
        srv.service_js = self.content
        srv.save()
