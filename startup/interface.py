import re
try:
    import config
except ImportError:
    from pathlib import Path
    import os
    import sys
    PROJ_DIR = str(Path(os.path.dirname(os.path.abspath(__file__))).parent)
    sys.path.insert(0, PROJ_DIR)
    import config
from bs4 import BeautifulSoup, SoupStrainer

from startup.get.interface import get_data_or_error
from startup.get.methods.to_file import write_to_parsed_file

def get_parsed_list():
    data, persistent = get_data_or_error()
    #data, persistent = '1 title1\n2 title2\n3 title3\n', True
    if persistent:
        # handle parsed data
        split_lines = data.splitlines()
        parsed_list = []
        for line in split_lines:
            parsed_list.append((line.split()[0], ' '.join(line.split()[1:])))
        return parsed_list
    else:
        #handle html data
        soup = BeautifulSoup(data, 'html.parser', parse_only=SoupStrainer(id='numerical-index'))

        matches = []
        for single_pep_tr in soup.tbody.find_all('tr'):
            single_pep_data = single_pep_tr.find_all('td')
            match = single_pep_data[1].text, single_pep_data[2].text
            matches.append(match)
        write_to_parsed_file(matches)
        #matches = re.findall(config.PEP_REGEXP, str(soup), re.I)
        #with open(config.PEP_PARSED_FILE, 'w') as parsed_file:
        #    for num, title in matches:
        #        parsed_file.write('%s %s\n' % (num, title))
        #        parsed_file.write('{} {}\n'.format(num, title))
        return matches

#<tr><td>P</td>
#<td class="num"><a class="reference external" href="/dev/peps/pep-0001">1</a></td>
#<td>PEP Purpose and Guidelines</td>
#<td>Warsaw, Hylton, Goodger, Coghlan</td>
#</tr>

if __name__ == '__main__':
    print(get_parsed_list())
