"""
This module is for save
and manipule the configuration
of the server, also have the server.
Execute the server with the file 'index.py'

"""

from flask import Flask
from routes.converter import converter
from helpers.config import CONFIG

# creating
app = Flask(__name__)

# settings
app.secret_key = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = CONFIG['UPLOAD_FOLDER']

# using the routes
app.register_blueprint(converter)