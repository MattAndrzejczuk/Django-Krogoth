import os
from LazarusV.super_hpi.hpi_vanilla_cavedog import CAVEDOG_WEAPONS, CAVEDOG_FEATURES, CAVEDOG_SFX, CAVEDOG_3DO, \
    CAVEDOG_GAF, CAVEDOG_UNITS

from LazarusV.super_hpi.hpi_build_assembly import totala_assembler


class SuperHPI():
    def __init__(self, dump_path: str):

        self.base_dir = dump_path
        self.rawWeaponFiles = ""
        self.rawUnitFiles = ""
        self.rawFeatureFiles = ""
        self.rawDownloadFiles = ""

        self.VANILLA_PATH = 'hpi_vanilla/'
        self.logFbiUnitsProcessed = 0

        self._3d_model_dependencies = {}
        self._3d_model_dependencies_cavedog = {}
        self._3d_model_dependencies_error = {}
        self._gaf_dependencies = {}
        self._gaf_dependencies_cavedog = {}
        self._gaf_dependencies_error = {}
        self._wav_dependencies = {}
        self._wav_dependencies_cavedog = {}
        self._wav_dependencies_error = {}

        self.debug_specific_object_mode = False
        self.strict_mode = True
        self.output_dir = '!!!'

        self.cavedog_data_base = totala_assembler(strict_mode=self.strict_mode)
        self.all_readonly_assets = {}
        self.units_with_errors = []



    def loadRawFilesToRAM(self):
        units_path = self.base_dir + 'units/'
        weapons_path = self.base_dir + 'weapons/'
        features_path = self.base_dir + 'features/'
        downloads_path = self.base_dir + 'downloads/'

        if os.path.exists(allFbiFilesPath):
            unitFiles = os.listdir(allFbiFilesPath)
            for fileName in unitFiles:
                cleanFBI = self.cleanFbi(allFbiFilesPath + fileName)
                self.allAppendedUnitFBIs += cleanFBI
        if os.path.exists(weaponsPath):
            weaponfiles = os.listdir(weaponsPath)
            for fileName in weaponfiles:
                self.allAppendedWeaponTDFs += self.cleanTdf(weaponsPath + fileName)
        if os.path.exists(featuresPath):
            featureFiles = os.listdir(featuresPath)
            for fileName in featureFiles:
                cleanTDF = self.cleanTdf(featuresPath + fileName)
                self.allAppendedFeatureTDFs += cleanTDF
        if os.path.exists(downloads_path):
            downloadFiles = os.listdir(downloads_path)
            for fileName in downloadFiles:
                cleanTDF = self.cleanTdf(downloads_path + fileName)
                self.allAppendedDownloadTDFs += cleanTDF