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
    """[summary]

    Args:
        context ([type]): [description]
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_route():
    """[summary]

    Returns:
        [type]: [description]
    """
    stateDict = storage.all(State)

    return render_template('9-states.html', stateDict=stateDict)


@app.route('/states/<id>', strict_slashes=False)
def state_id_route(id):
    """[summary]

    Args:
        id ([type]): [description]

    Returns:
        [type]: [description]
    """
    stateDict = storage.all(State)
    try:
        state = stateDict.get("State.{}".format(id))
        return render_template('9-states.html', state=state)
    except:
        return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
