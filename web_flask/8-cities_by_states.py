#!/usr/bin/python3
""" starts app for 7 """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def storage_close(self):
    """[summary]
    """
    storage.close()


@app.route('/cities_by_states')
def cities_list():
    """[summary]

    Returns:
        [type]: [description]
    """
    stateList = storage.all(State)

    return render_template('8-cities_by_states.html', all_states=stateList)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
