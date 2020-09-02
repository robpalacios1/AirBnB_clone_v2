#!/usr/bin/python3
"""Start web application with two routings
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Removes current SQLAlchemy session."""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def route1():
    """Display HTML page with a list of
    all objects inside a DBstorage."""
    url = '7-states_list.html'
    dictionary = storage.all("State")
    return render_template(url, states=dictionary)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
