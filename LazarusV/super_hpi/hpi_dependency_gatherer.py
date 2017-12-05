
from LazarusV.super_hpi.hpi_analyzer import TotalASuperHPI


class TotalACompileManager():

    def __init__(self, root_fbi_path: str):
        self.allModFBIs = []
        self.allModTDFs = {}
        self.allModFeatures = {}
        self.allModDownloads = {}
        self.modHPI = TotalASuperHPI(dump_path=root_fbi_path)