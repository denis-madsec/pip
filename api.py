from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_pymongo import PyMongo
import re
from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/python"
mongo = PyMongo(app)

peps = [
    {
        "_id" : "5b72b17b2af629417c4ad486",
        "title" : "PEP Purpose and Guidelines",
        "number" : "1"
    },
    {
        "_id" : "5b72b17b2af629417c4ad487",
        "title" : "Procedure for Adding New Modules",
        "number" : "2"
    },
    {
        "_id" : "5",
        "title" : "ProcedureModules",
        "number" : "22"
    }
]

def make_public_pep(pep):
    new_pep = {}
    for field in pep:
        if field == "_id":
            new_pep["uri"] = url_for('get_pep', pep_id=pep["_id"], _external=True)
            #new_pep[field] = pep[field]
        else:
            new_pep[field] = pep[field]
    return new_pep


@app.route('/api/peps', methods=['GET'])
def get_peps():
    return jsonify({'peps' : [make_public_pep(pep) for pep in peps]})

@app.route('/api/peps', methods=['POST'])
def update_db():
    if not request.json:
        abort(400)
    pep = {
        '_id' : str(len(peps)),
        'title' : request.json['title'],
        'number' : request.json['number']
    }
    peps.append(pep)
    return jsonify({'pep': pep}), 201

@app.route('/api/peps/search/<pep_title>', methods=['GET'])
def search_for_pep_by_title(pep_title):
    regex = re.compile(pep_title, re.IGNORECASE)
    matches = mongo.db.peps.find({'title' : {'$regex' : regex } }, {'_id': 0} )
    return  jsonify(list(matches))

@app.route('/api/peps/<pep_id>', methods=['GET'])
def get_pep(pep_id):
    #return the pep with the matching id
    pep = [pep for pep in peps if pep['_id'] == pep_id]
    if not pep:
        abort(404)
    return jsonify({'pep': pep[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

if __name__ == '__main__':
    app.run(debug=True)
