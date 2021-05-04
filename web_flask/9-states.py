#!/usr/bin/python3
""" starts app for 7 """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from sqlalchemy import orm
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(context):
    """ Method to remove current SQLAlchemy Session """
    storage.close()


@app.route('/states')
def state_route():
    """[summary]
    """
    state_dict = storage.all(State)
    return render_template('9-states.html', state_dict=state_dict)


@app.route('/states/<id>')
def state_id_route(id):
    """[summary]

    Args:
        id ([type]): [description]
    """
    state_dict = storage.all(State)
    try:
        state = state_dict.get("State.{}".format(id))
    except:
        return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
