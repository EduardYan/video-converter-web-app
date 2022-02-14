"""
This module is for save
and manipule the configuration
of the server, also have the server.
Execute the server with the file 'index.py'

"""

from flask import Flask
from routes.converter import converter

# creating
app = Flask(__name__)

# using the routes
app.register_blueprint(converter)