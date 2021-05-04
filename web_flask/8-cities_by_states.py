#!/usr/bin/python3
""" starts app for 7 """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(context):
    '''Method to remove current SQLAlchemy Session'''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_route():
    '''Method to load all cities of a State'''

    stateList = storage.all(State)

    return render_template('8-cities_by_states.html', stateList=stateList)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
