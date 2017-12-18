# coding=utf-8
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'
from krogoth_core.models import *


class KrogothCore(object):

    def __init__(self, theme_name: str):
        self._theme = theme_name

    def install_ad_hoc_theme(self):
        for file in files:
            arr = file.split('.')
            print('- - - - - - - - - - - ' + str(len(arr)))
            print(arr[0])
            print(arr[len(arr) - 2])
            print(arr[len(arr) - 1])


    def install_theme(self):
        core_config = AKFoundationCoreConfig.objects.get_or_create(is_selected_theme=True,
                                                                   name='core.config',
                                                                   ext='.js')
