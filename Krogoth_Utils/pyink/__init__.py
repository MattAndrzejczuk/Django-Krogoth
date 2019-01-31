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
    def print_blue(cls, log, _e):
        print(cls.lightblue, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_darkblue(cls, log, _e):
        print(cls.blue, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_red(cls, log, _e):
        print(cls.red, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_lightred(cls, log, _e):
        print(cls.lightred, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_orange(cls, log, _e):
        print(cls.orange, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_green(cls, log, _e):
        print(cls.lightgreen, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_pink(cls, log, _e):
        print(cls.pink, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_yellow(cls, log, _e):
        print(cls.yellow, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_cyan(cls, log, _e):
        print(cls.cyan, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_purple(cls, log, _e):
        print(cls.purple, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_lightcyan(cls, log, _e):
        print(cls.lightcyan, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_gray(cls, log, _e):
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

        print(FAIL + "FAIL" + ENDC)
        print(BOLD + "BOLD" + ENDC)
        print(UNDERLINE + "UNDERLINE" + ENDC)
        print(TEAL + "TEAL" + ENDC)
        print(BLACK + "BLACK" + ENDC)
        print(GRAY + "GRAY" + ENDC)
        print(black + "black" + ENDC)
        print(red + "red" + ENDC)
        print(green + "green" + ENDC)
        print(orange + "orange" + ENDC)
        print(blue + "blue" + ENDC)
        print(purple + "purple" + ENDC)
        print(cyan + "cyan" + ENDC)
        print(lightgrey + "lightgrey" + ENDC)
        print(darkgrey + "darkgrey" + ENDC)
        print(lightred + "lightred" + ENDC)
        print(lightgreen + "lightgreen" + ENDC)
        print(yellow + "yellow" + ENDC)
        print(lightblue + "lightblue" + ENDC)
        print(pink + "pink" + ENDC)
        print(lightcyan + "lightcyan" + ENDC)

    '\033['

    @classmethod
    def print_everything_possible(cls):
        this_ink = '\033[91m'
        i = 0
        while i < 100:
            print(i, end=" \033[" + str(i) + "m -~=[" + str(i) + "]=~- \n")
            i += 1
