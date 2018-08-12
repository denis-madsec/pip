import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
PEP_HTML_FILE = os.path.join(DATA_DIR, 'pep.html')
PEP_PARSED_FILE = os.path.join(DATA_DIR, 'pep.txt')
PEP_WEBPAGE = 'https://www.python.org/dev/peps/'
PEP_REGEXP = r'href=.+>(\w+)</a></td>\n<td>(.*)</td>'
