# from krogoth_admin.models import KrogothServerLoggedModel
# from pyink import ink






class LogUsage():

    def __init__(self, str1, str2, str3):
        print("\033[36m" + "\t\t▣▶︎ " + "\033[0m", end="\033[94m")
        print(str1, end="\033[0m")
        print("\033[35m" + " ║ " + "\033[0m", end="\033[91m")
        print(str2, end="\033[0m")
        print("\033[35m" + " ︎║ " + "\033[0m", end="\033[32m")
        print(str3, end="\033[0m")
        print("\033[96m" + " ◉ " + "\033[0m", end="\n")
