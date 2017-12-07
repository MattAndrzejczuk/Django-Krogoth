import os
from LazarusV.super_hpi.hpi_V_vanilla_cavedog import CAVEDOG_WEAPONS, CAVEDOG_FEATURES, CAVEDOG_SFX, CAVEDOG_3DO, \
    CAVEDOG_GAF, CAVEDOG_UNITS

from LazarusV.super_hpi.hpi_III_build_assembly import TotalAAssembler
from LazarusV.super_hpi.hpi_III_build_disassembler import TotalADisassembler


class TotalASuperHPI(object):

    def __init__(self, dump_path: str):
        self.base_dir = dump_path
        self._disassembler = TotalADisassembler(dump_path=dump_path)
        self._assembler = TotalAAssembler(strict_mode=True)
        self._disassembled_units = []
        self._disassembled_weapons = {}
        self._disassembled_features = {}
        self._disassembled_downloads = {}
        super().__init__()
        self.finalize_disassembly()
    
    @property 
    def disassembler(self) -> TotalADisassembler:
        return self._disassembler
    @property
    def disassembled_units(self) -> list:
        return self._disassembled_units
    @property
    def disassembled_weapons(self) -> dict:
        return self._disassembled_weapons
    @property
    def disassembled_features(self) -> dict:
        return self._disassembled_features
    @property
    def disassembled_downloads(self) -> dict:
        return self._disassembled_downloads
    
    def finalize_disassembly(self):
        str_units = self._disassembler.unload_text_units
        str_weapons = self._disassembler.unload_text_weapons
        str_features = self._disassembler.unload_text_features
        str_downloads = self._disassembler.unload_text_downloads
        self._disassembled_units = self._disassembler.get_disassembled_units(from_text=str_units)
        self._disassembled_weapons = self._disassembler.get_disassembled_weapons(from_text=str_weapons)
        self._disassembled_features = self._disassembler.get_disassembled_generic(from_text=str_features, kind='feature')
        self._disassembled_downloads = self._disassembler.get_disassembled_generic(from_text=str_downloads, kind='download')

    def save_disassembly_to_sql(self):
        pass