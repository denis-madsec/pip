try:
    import config
except ImportError:
    from pathlib import Path
    import os
    import sys
    PROJ_DIR = str(Path(os.path.dirname(os.path.abspath(__file__))).parent)
    sys.path.insert(0, PROJ_DIR)
    import config



def write_to_parsed_file(data):
    with open(config.PEP_PARSED_FILE, 'w') as parsed_file:
    #with open('/home/denis/projects/test/data/pep.txt', 'w') as parsed_file:
        for num, title in data:
            parsed_file.write('{} {}\n'.format(num, title))
