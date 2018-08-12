import os

def get_data_from_file(path):
    if os.path.isfile(path):
        with open(path) as fd:
            return True, fd.read()
    else:
        return False, None
