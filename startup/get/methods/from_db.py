from pymongo import MongoClient
import re

def get_db_connection():
    client = MongoClient()
    db = client.python
    return db

def get_pep_by_name(pep_title):
    db = get_db_connection()

    regex = re.compile(pep_title, re.IGNORECASE)
    matches = db.peps.find( {'title' : {'$regex' : regex } } )
    ret = []
    for match in matches:
        ret.append(match[title], match[number])
    return ret
