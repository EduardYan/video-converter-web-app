"""
This file have the routes
to use in the server.
"""


from flask import Blueprint, render_template

# routes
converter = Blueprint('converter', __name__)

@converter.route('/')
def initial():
  """
  Initial route
  for the server.
  """

  return 'runing'


@converter.route('/about')
def about():
  """
  Route for render the about page.
  """

  return 'about'