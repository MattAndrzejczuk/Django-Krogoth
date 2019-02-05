import os

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
    def p_blue(cls, log, _e="\n"):
        print(cls.lightblue, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def p_blue_dark(cls, log, _e="\n"):
        print(cls.blue, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def p_red_dark(cls, log, _e="\n"):
        print(cls.red, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def p_red(cls, log, _e="\n"):
        print(cls.lightred, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def print_orange(cls, log, _e="\n"):
        print(cls.orange, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def print_green(cls, log, _e="\n"):
        print(cls.lightgreen, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def print_pink(cls, log, _e="\n"):
        print(cls.pink, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def print_yellow(cls, log, _e="\n"):
        print(cls.yellow, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def print_cyan(cls, log, _e="\n"):
        print(cls.cyan, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def print_purple(cls, log, _e="\n"):
        print(cls.purple, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def print_lightcyan(cls, log, _e="\n"):
        print(cls.lightcyan, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")

    @classmethod
    def print_gray(cls, log, _e="\n"):
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

    @classmethod
    def print_everything_possible(cls):
        os.system("clear")
        this_ink = '\033[91m'
        i = 0
        while i < 150:
            if i < 108 and i > 89:
                print(cls.ENDC, end=" \033[" + str(i) + "m ◀█\\033[" + str(i) + "m█▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
                print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + cls.ENDC)
                print("\033[" + str(i+1) + "m", end='')
                print()
            elif i < 48 and i > 30:
                print(cls.ENDC, end=" \033[" + str(i) + "m ◀█\\033[" + str(i) + "m█▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
                print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + cls.ENDC)
                print("\033[" + str(i+1) + "m", end='')
                print()
            elif i < 48 and i > 30:
                print(cls.ENDC, end=" \033[" + str(i) + "m ◀█\\033[" + str(i) + "m█▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
                print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + cls.ENDC)
                print("\033[" + str(i+1) + "m", end='')
                print()
            elif i > 0 and i < 9:
                print(cls.ENDC, end=" \033[" + str(i) + "m ◀█\\033[" + str(i) + "m█▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
                print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + cls.ENDC)
                print("\033[" + str(i+1) + "m", end='')
                print()
            i += 1

ink.print_everything_possible()
