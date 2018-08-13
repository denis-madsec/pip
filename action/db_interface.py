from pymongo import MongoClient
import re
from startup.interface import get_parsed_list


def get_db_connection():
    client = MongoClient()
    db = client.python
    return db


def search_db(pep_title):
    db = get_db_connection()

    regex = re.compile(pep_title, re.IGNORECASE)
    matches = db.peps.find({'title' : {'$regex' : regex } } )
    ret = []
    for match in matches:
        ret.append((match['title'], match['number']))
        print(match['title'], match['number'])
    return ret


def clear_db(db):
    #db = get_db_connection()
    db.peps.delete_many({})


def update_db():
    peps = get_parsed_list()
    db = get_db_connection()
    clear_db(db)
    for pep in peps:
        pep_doc = {
            'title' : pep[1],
            'number' : pep[0]
        }
        db.peps.insert_one(pep_doc)
    print('db.peps now has', db.peps.find({}).count(), 'docs')
