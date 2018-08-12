import config
from startup.get.methods.from_file import get_data_from_file
from startup.get.methods.from_web import get_data_from_web

def get_data_or_error():
    persistent = False
    ok, data = get_data_from_web(config.PEP_WEBPAGE)
    #ok, data = get_data_from_file(config.PEP_HTML_FILE)    #for testing purposes
    if not ok:
        persistent = True
        ok, data = get_data_from_file(config.PEP_PARSED_FILE)
        if not ok:
            raise IOError('Couldn\'t find files.')
    return data, persistent
