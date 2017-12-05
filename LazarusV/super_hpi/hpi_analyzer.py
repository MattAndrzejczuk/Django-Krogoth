import os
from LazarusV.super_hpi.hpi_vanilla_cavedog import CAVEDOG_WEAPONS, CAVEDOG_FEATURES, CAVEDOG_SFX, CAVEDOG_3DO, \
    CAVEDOG_GAF, CAVEDOG_UNITS

from LazarusV.super_hpi.hpi_build_assembly import TotalAAssembler
from LazarusV.super_hpi.hpi_string_parser import TotalADisassembler


class TotalASuperHPI():
    def __init__(self, dump_path: str):

        self.base_dir = dump_path
        self._disassembler = TotalADisassembler(dump_path=dump_path)
        self.cavedog_data_base = TotalAAssembler(strict_mode=True)

        self.disassembled_units = []
        self.disassembled_weapons = {}
        self.disassembled_features = {}
        self.disassembled_downloads = {}

        self.VANILLA_PATH = 'hpi_vanilla/'

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


        self.all_readonly_assets = {}
        self.units_with_errors = []



    def finalize_disassembly(self):
        self.disassembled_units = self._disassembler.get_disassembled_units(self._disassembler.unload_text_units)
        self.allModTDFs = self.modHPI.splitWeaponClusterTDF(self.modHPI.allAppendedWeaponTDFs)
        self.allModFeatures = self.modHPI.splitGenericClusterTDF(self.modHPI.allAppendedFeatureTDFs, 'feature')
        self.allModDownloads = self.modHPI.splitGenericClusterTDF(self.modHPI.allAppendedDownloadTDFs, 'download')