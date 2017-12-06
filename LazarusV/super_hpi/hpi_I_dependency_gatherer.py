
from LazarusV.super_hpi.hpi_analyzer import TotalASuperHPI


class TotalACompileManager(object):

    def __init__(self, root_fbi_path: str):
        # - - - - - - - - - - - - - - -
        # 3.) save disassembled to SQL***
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # 1.) preload disassembled from SQL***
        # 2.) build assembly SQL~>File***
        # 3.) compress assembly***
        # - - - - - - - - - - - - - - -
        self._superHPI = TotalASuperHPI(dump_path=root_fbi_path)

    @property
    def superHPI(self) -> TotalASuperHPI:
        return self._superHPI