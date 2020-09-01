#!/usr/bin/python3
"""List cities by states Module"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states_list():
    """display a HTML the States and cities by states"""
    all_states = list(storage.all(State).values())
    return (render_template('8-cities_by_states.html', all_states=all_states))


@app.teardown_appcontext
def teardown(self):
    """function that call close methofd"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
