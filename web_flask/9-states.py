#!/usr/bin/python3
"""List cities by states Module"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states_list(id=None):
    """display States, object found by id State and its cities"""
    all_states = storage.all(State).values()
    if id:
        _id = id
        id_state = None
        for state in all_states:
            if state.id == _id:
                id_state = state
                break
    else:
        id_state = list(all_states)
    return (render_template('9-states.html', **locals()))


@app.teardown_appcontext
def teardown(self):
    """function that call close methofd"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
