import sys
import re
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
PEP_HTML_FILE = os.path.join(DATA_DIR, 'pep.html')
PEP_PARSED_FILE = os.path.join(DATA_DIR, 'pep.txt')
PEP_WEBPAGE = 'https://www.python.org/dev/peps/'
PEP_REGEXP = r'href=.+>(\w+)</a></td>\n<td>(.*)</td>'

def get_data_from_file(path):
    if os.path.isfile(path):
        with open(path) as fd:
            return True, fd.read()
    else:
        return False, None

def get_data_from_web(webpage):


def get_data_or_error():
    persistent = True
    ok, data = get_data_from_file(PEP_PARSED_FILE)
    if not ok:
        persistent = False
        ok, data = get_data_from_file(PEP_HTML_FILE)
        if not ok:
            ok, data = get_data_from_web(PEP_WEBPAGE)
            if not ok:
                raise IOError('Couldn\'t find files.')

    return data, persistent

def get_parsed_list():
    data, persistent = get_data_or_error()

    if persistent:
        # handle parsed data
        split_lines = data.splitlines()
        parsed_list = []
        for line in split_lines:
            parsed_list.append((line.split()[0], ' '.join(line.split()[1:])))
        return parsed_list
    else:
        #handle html data
        matches = re.findall(PEP_REGEXP, data, re.I)
        with open(PEP_PARSED_FILE, 'w') as parsed_file:
            for num, title in matches:
                #parsed_file.write('%s %s\n' % (num, title))
                parsed_file.write('{} {}\n'.format(num, title))
        return matches


def find_pep_by_name(partial_name, parsed_list):
    if partial_name and parsed_list:

        for num, title in parsed_list:
            match = re.search(partial_name, title, re.I)
            if match:
                print(title, num)
        print()


def get_user_input(args):
    if args:
        return args[0]
    else:
        return input('Enter your the pep name: ')



def main():

    args = sys.argv[1:]
    partial_name = get_user_input(args)

    parsed_list = get_parsed_list()

    find_pep_by_name(partial_name, parsed_list)

if __name__ == '__main__':
    main()
