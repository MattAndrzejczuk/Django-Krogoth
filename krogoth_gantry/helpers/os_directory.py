import os

class MoveToNewDirectory(object):
    def __init__(self, old_path: str, new_path: str):
        super(MoveToNewDirectory, self).__init__()
        cmd = 'mv "' + old_path + '" "' + new_path + '"'
        os.system(cmd)
