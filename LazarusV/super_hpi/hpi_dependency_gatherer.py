
from LazarusV.super_hpi.hpi_analyzer import TotalASuperHPI


class TotalACompileManager():

    def __init__(self, root_fbi_path: str):
        # self.allModFBIs = []
        # self.allModTDFs = {}
        # self.allModFeatures = {}
        # self.allModDownloads = {}

        # - - - - - - - - - - - - - - -
        # 1.) preload dump dir
        # 2.) disassemble
        # 3.) save disassembled to SQL***
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # 1.) preload disassembled from SQL***
        # 2.) build assembly SQL~>File***
        # 3.) compress assembly***
        # - - - - - - - - - - - - - - -
        self.modHPI = TotalASuperHPI(dump_path=root_fbi_path)
