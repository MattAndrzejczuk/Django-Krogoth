# from jawn.console_printer import CentralCheckpoint

class MetaGenerator():
    @classmethod
    def determine_meta_data(cls, filename: str) -> list:
        # CentralCheckpoint.log('MetaGenerator', filename)
        test = "META_" + filename + "_ITWORKS"
        return [test, test, test]
