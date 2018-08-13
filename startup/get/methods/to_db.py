from pymongo import MongoClient

def get_db_connection():
    client = MongoClient()
    db = client.python
    return db

def clear_db(db):
    #db = get_db_connection()
    db.peps.delete_many({})

def update_db(peps):
    db = get_db_connection()
    clear_db(db)
    for pep in peps:
        pep_doc = {
            'title' : pep[0]
            'number' : pep[1]
        }
        db.peps.insert_one(pep_doc)
