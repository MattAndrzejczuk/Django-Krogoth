import os, errno
from krogoth_gantry.management.commands.installdjangular import bcolors

class MoveToNewDirectory(object):
    def __init__(self, old_path: str, new_path: str):
        super(MoveToNewDirectory, self).__init__()
        cmd = 'mv "' + old_path + '" "' + new_path + '"'
        os.system(cmd)
        print(bcolors.TEAL + bcolors.UNDERLINE + cmd + bcolors.ENDC + bcolors.ENDC)
