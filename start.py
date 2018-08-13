import sys
import os

PROJ_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ_DIR)

from startup.interface import get_parsed_list
from action.finder import find_pep_by_name
from action.from_db import search_db
from action.to_db import update_db

def get_user_input(args):
    if args:
        return args[0]
    else:
        return input('Enter your the pep name: ')


def main():

    args = sys.argv[1:]
    if not args:
        print("usage: [--fromweb pep] or [--fromdb pep] or [--update]")
        sys.exit(1)
    if args[0] == "--fromweb":
        parsed_list = get_parsed_list()
        partial_name = get_user_input(args[1:])
        find_pep_by_name(partial_name, parsed_list)
    elif args[0] == '--fromdb':
        partial_name = get_user_input(args[1:])
        search_db(partial_name)
    elif args[0] == '--update':
        update_db()
    else:
        print("incorrect usage!")
        sys.exit(1)


    #partial_name = get_user_input(args)

    #parsed_list = get_parsed_list()

    #find_pep_by_name(partial_name, parsed_list)

if __name__ == '__main__':
    main()
