from utils.fixtures.pyink import ink



class CentralCheckpoint:

    @classmethod
    def pass_instance(cls, instance):
        ink.print_lightcyan("instance", ink.p_blue_dark("⥤ "))
        ink.print_purple(instance.__class__.__name__, "")
        ink.print_yellow(" ▷▓▓▓▓▓▓▓▓▓▓▓▓▶︎ ", ink.p_blue("╔"))
        ink.print_orange(instance.__name__, ink.p_blue("╗"))

    @classmethod
    def log(cls, n1, n2):
        ink.print_lightcyan("instance", ink.p_blue_dark("⥤ "))
        ink.print_purple(n1, "")
        ink.print_yellow(" ▷▓▓▓▓▓▓▓▓▓▓▓▓▶︎ ", ink.p_blue("╔"))
        for element in n2:
            ink.print_orange(element, ink.p_blue("╗"))