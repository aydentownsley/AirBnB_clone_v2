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


@app.route('/states_list')
def states_list():
    """[summary]

    Returns:
        [type]: [description]
    """
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', all_states=all_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
