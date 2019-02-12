from jawn.settings import KROGOTH_TRACE




def krogoth_trace_class(func):
    def wrapper(self, *args):
        if KROGOTH_TRACE:
            print("\033[92m \033[0m \033[32m▓" + func.__name__, end="▓\033[0m")
            for a in args:
                print("\033[36m⥤", end="\033[92m ╔\033[0m\033[91m\033[0m")
                print(a, end="╦\033[92m\033[0m")
                print("╗\033[0m", end="")
        func(self, *args)
        if KROGOTH_TRACE:
            print("\033[33m FINISHED: \033[0m" + func.__name__, end="")
            print("", end="\033[33m ▣ \033[0m")
    return wrapper

