"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
import sys
sys.path.append('/Modules')

from Modules import MatSetP
from Modules import MatSetPF
from Modules import MSetQmode

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Welcome to Virtual Lab API"

@app.route('/matsetp/<string:field2>')
def matSetP(field2):
    return MatSetP.matSetP(field2);

@app.route('/matsetpf/<string:field1>')
def matSetPF(field1):
    return MatSetPF.matSetPF(field1);

@app.route('/matSetQmode/<string:field3>')
def matSetQmode(field3):
    return MSetQmode.matSetQmode(field3);

@app.route('/test/<string:name>')
def test(name):    
    return "the name is: " + name


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8585'))
    except ValueError:
        PORT = 8585
    app.run(HOST, PORT)
