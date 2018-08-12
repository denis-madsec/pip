import re

def find_pep_by_name(partial_name, parsed_list):
    if partial_name and parsed_list:

        for num, title in parsed_list:
            match = re.search(partial_name, title, re.I)
            if match:
                print(title, num)
        print()
