# Matt Andrzejczuk (c) 2018
# MIT License



class ink:
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TEAL = '\033[96m'
    BLACK = '\033[97m'
    GRAY = '\033[90m'

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    LIGHT_YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GREY = '\033[37m'

    DARKGREY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    PINK = '\033[95m'
    LIGHT_CYAN = '\033[96m'

    @classmethod
    def p_BLUE(cls, log, _e=""):
        print(cls.LIGHT_BLUE, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def p_BLUE_DARK(cls, log, _e=""):
        print(cls.BLUE, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def p_RED_DARK(cls, log, _e=""):
        print(cls.RED, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def p_RED(cls, log, _e="\n"):
        print(cls.LIGHT_RED, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_YELLOW(cls, log, _e=""):
        print(cls.YELLOW, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_GREEN(cls, log, _e=""):
        print(cls.LIGHT_GREEN, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_PINK(cls, log, _e=""):
        print(cls.PINK, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_YELLOW(cls, log, _e=""):
        print(cls.YELLOW, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_CYAN(cls, log, _e=""):
        print(cls.CYAN, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_PURPLE(cls, log, _e=""):
        print(cls.PURPLE, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_LIGHT_CYAN(cls, log, _e=''):
        print(cls.LIGHT_CYAN, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_gray(cls, log, _e=""):
        print(cls.GRAY, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def help_examples(cls):
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        TEAL = '\033[96m'
        BLACK = '\033[97m'
        GRAY = '\033[90m'
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        LIGHT_GREY = '\033[37m'
        DARKGREY = '\033[90m'
        LIGHT_RED = '\033[91m'
        LIGHT_GREEN = '\033[92m'
        YELLOW = '\033[93m'
        LIGHT_BLUE = '\033[94m'
        PINK = '\033[95m'
        LIGHT_CYAN = '\033[96m'

        print(FAIL + "FAIL" + ENDC)
        print(BOLD + "BOLD" + ENDC)
        print(UNDERLINE + "UNDERLINE" + ENDC)
        print(TEAL + "TEAL" + ENDC)
        print(BLACK + "BLACK" + ENDC)
        print(GRAY + "GRAY" + ENDC)
        print(BLACK + "BLACK" + ENDC)
        print(RED + "RED" + ENDC)
        print(GREEN + "GREEN" + ENDC)
        print(YELLOW + "YELLOW" + ENDC)
        print(BLUE + "BLUE" + ENDC)
        print(PURPLE + "PURPLE" + ENDC)
        print(CYAN + "CYAN" + ENDC)
        print(LIGHT_GREY + "LIGHT_GREY" + ENDC)
        print(DARKGREY + "DARKGREY" + ENDC)
        print(LIGHT_RED + "LIGHT_RED" + ENDC)
        print(LIGHT_GREEN + "LIGHT_GREEN" + ENDC)
        print(YELLOW + "YELLOW" + ENDC)
        print(LIGHT_BLUE + "LIGHT_BLUE" + ENDC)
        print(PINK + "PINK" + ENDC)
        print(LIGHT_CYAN + "LIGHT_CYAN" + ENDC)

    '\033['

    @classmethod
    def print_everything_possible(cls):
        this_ink = '\033[91m'
        i = 0
        while i < 150:
            print(i, end=" \033[" + str(i) + "m -~=[" + str(i) + "]=~- \n")
            i += 1
