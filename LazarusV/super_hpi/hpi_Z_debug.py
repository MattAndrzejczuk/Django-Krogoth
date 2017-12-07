import json
from LazarusV.super_hpi.hpi_I_dependency_gatherer import TotalACompileManager
from LazarusV.super_hpi.hpi_III_build_disassembler import TotalADisassembler
from LazarusV.super_hpi.hpi_II_analyzer import TotalASuperHPI

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
TEAL = '\033[96m'
BLACK = '\033[97m'
GRAY = '\033[90m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'


class logged_disassembler(object):
    def __init__(self):
        test_path = '/usr/src/persistent/media/Processed_HPI_Archives/root/ArmPrime_1.0_mattsAbel/'
        self._ta_compile_manager = TotalACompileManager(root_fbi_path=test_path)

    def dump_all(self):
        units = self.get_units
        weapons = self.get_weapons
        features = self.get_features
        downloads = self.get_downloads
        print(units)
        print(weapons)
        print(features)
        print(downloads)

    @property
    def get_units(self) -> str:
        return self.colored_blue(self.json_pretty(self._ta_compile_manager.superHPI.disassembled_units))
    @property
    def get_weapons(self) -> str:
        return self.colored_red(self.json_pretty(self._ta_compile_manager.superHPI.disassembled_weapons))
    @property
    def get_features(self) -> str:
        return self.colored_orange(self.json_pretty(self._ta_compile_manager.superHPI.disassembled_features))
    @property
    def get_downloads(self) -> str:
        return self.colored_green(self.json_pretty(self._ta_compile_manager.superHPI.disassembled_downloads))


    @property
    def core1_compiler(self) -> TotalACompileManager:
        return self._ta_compile_manager
    @property
    def core2_super_hpi(self) -> TotalASuperHPI:
        return self._ta_compile_manager.superHPI
    @property
    def core3_disassembler(self) -> TotalADisassembler:
        return self._ta_compile_manager.superHPI.disassembler


    @staticmethod
    def colored_blue(text) -> str:
        return lightblue + text + ENDC
    @staticmethod
    def colored_green(text) -> str:
        return green + text + ENDC
    @staticmethod
    def colored_red(text) -> str:
        return red + text + ENDC
    @staticmethod
    def colored_orange(text) -> str:
        return orange + text + ENDC
    @staticmethod
    def colored_purple(text) -> str:
        return purple + text + ENDC
    @staticmethod
    def json_pretty(dictionary) -> str:
        return json.dumps(dictionary, indent=2, sort_keys=True)

"""
from LazarusV.super_hpi.hpi_Z_debug import logged_disassembler
test = logged_disassembler()

units = test.get_units
weapons = test.get_weapons
features = test.get_features
downloads = test.get_downloads
"""