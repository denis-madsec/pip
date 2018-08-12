import sys
import os

PROJ_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ_DIR)

from startup.interface import get_parsed_list
from action.finder import find_pep_by_name

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
