from pymongo import MongoClient
import re
from startup.interface import get_parsed_list


def get_db_connection():
    client = MongoClient()
    db = client.python
    return db


def db_decorator(function):
    def wrapper(*args, **kwargs):
        client = MongoClient()
        db = client.python
        function(db, *args, **kwargs)
        db.client.close()
    return wrapper



@db_decorator
def search_db(db, pep_title):
    #db = get_db_connection()

    regex = re.compile(pep_title, re.IGNORECASE)
    matches = db.peps.find({'title' : {'$regex' : regex } } )
    ret = []
    for match in matches:
        ret.append((match['title'], match['number']))
        print(match['title'], match['number'])
    db.client.close()
    return ret


def clear_db(db):
    #db = get_db_connection()
    db.peps.delete_many({})

@db_decorator
def update_db(db):
    peps = get_parsed_list()
    #db = get_db_connection()
    clear_db(db)
    for pep in peps:
        pep_doc = {
            'title' : pep[1],
            'number' : pep[0]
        }
        db.peps.insert_one(pep_doc)
    db.client.close()
    print('db.peps now has', db.peps.find({}).count(), 'docs')
