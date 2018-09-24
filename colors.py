class ink:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TEAL = '\033[96m'
    BLACK = '\033[97m'
    GRAY = '\033[90m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

    @classmethod
    def pblue(cls, log):
        print(cls.OKBLUE, end="")
        print(log, end="")
        print(cls.ENDC, end="")

    @classmethod
    def pred(cls, log):
        print(cls.lightred, end="")
        print(log, end="")
        print(cls.ENDC, end="")

    @classmethod
    def pgreen(cls, log):
        print(cls.lightgreen, end="")
        print(log, end="")
        print(cls.ENDC, end="")

    @classmethod
    def ppink(cls, log):
        print(cls.pink, end="")
        print(log, end="")
        print(cls.ENDC, end="")