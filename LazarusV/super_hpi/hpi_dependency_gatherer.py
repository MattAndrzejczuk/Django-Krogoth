
from LazarusV.super_hpi.hpi_analyzer import SuperHPI


class totala_compile_manager():

    def __init__(self, root_fbi_path: str):
        self.allModFBIs = []
        self.allModTDFs = {}
        self.allModFeatures = {}
        self.allModDownloads = {}
        self.modHPI = SuperHPI(dump_path=root_fbi_path)