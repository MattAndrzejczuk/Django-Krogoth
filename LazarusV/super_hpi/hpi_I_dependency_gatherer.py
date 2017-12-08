
from LazarusV.super_hpi.hpi_II_analyzer import TotalASuperHPI
from LazarusV.super_hpi.hpi_III_build_disassembler import TotalADisassembler
from LazarusV.super_hpi.hpi_III_build_assembly import TotalAAssembler
from LazarusIV.models import UploadRepository


# TODO: CompileManager is not a good name, maybe use: FreshAsset
class TotalACompileManager(object):

    def __init__(self, repo_base: UploadRepository):
        # - - - - - - - - - - - - - - -
        # 3.) save disassembled to SQL***
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # 1.) preload disassembled from SQL***
        # 2.) build assembly SQL~>File***
        # 3.) compress assembly***
        # - - - - - - - - - - - - - - -
        self._superHPI = TotalASuperHPI(repo=repo_base)

        # TODO: this doesn't belong here. This should only be used during publication and compile build
        self._compiler = TotalAAssembler(strict_mode=True)

    @property
    def superHPI(self) -> TotalASuperHPI:
        return self._superHPI

    @property
    def compiler(self) -> TotalAAssembler:
        return self._compiler
