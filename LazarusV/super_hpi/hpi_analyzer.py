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
        super().__init__()
        self.finalize_disassembly()


    def finalize_disassembly(self):
        str_units = self._disassembler.unload_text_units
        str_weapons = self._disassembler.unload_text_weapons
        str_features = self._disassembler.unload_text_features
        str_downloads = self._disassembler.unload_text_downloads
        self.disassembled_units = self._disassembler.get_disassembled_units(from_text=str_units)
        self.disassembled_weapons = self._disassembler.get_disassembled_weapons(from_text=str_weapons)
        self.disassembled_features = self._disassembler.get_disassembled_generic(from_text=str_features, kind='feature')
        self.disassembled_downloads = self._disassembler.get_disassembled_generic(from_text=str_downloads, kind='download')