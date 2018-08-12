import sys
import requests
#from bs4 import BeautifulSoup

def get_data_from_web(webpage):
    #with Session() as s:
    #    s.get(webpage)
    r = requests.get(webpage)

    #soup = BeautifulSoup(r.text, 'html.parser')
    #pep_table = soup.find(id='numerical-index')
    success, result = False, None
    if r.status_code == 200:
        success = True
        result = r.text

    return success, result


if __name__ == '__main__':
    PEP_WEBPAGE = 'https://www.python.org/dev/peps/'
    print(get_data_from_web(PEP_WEBPAGE))
