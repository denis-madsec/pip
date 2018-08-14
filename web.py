from flask import Flask
from action.db_interface import search_db
from startup.interface import get_parsed_list
from action.finder import find_pep_by_name

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello There!'

@app.route('/<source>/<pip_name>')
def display_pips(source, pip_name):
    if source == 'db':
        results = search_db(pip_name)
    elif source == 'web':
        parsed_list = get_parsed_list()
        print(parsed_list is not False)
        results = find_pep_by_name(pip_name, parsed_list)

    ret = '<h1>You searched for "{}" using {}:</h1>'.format(pip_name, source)
    ret += '<table style="width:100%"><tr><th>PEP Title</th><th>Number</th></tr>'
    for res in results:
        ret += '<tr><td>{}</td><td>{}</td></tr>'.format(res[0], res[1])
    ret += '</table>'
    return ret

if __name__ == '__main__':
    app.run(debug=True)
