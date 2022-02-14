"""
This file have some functions
for work with the configuration
of the server.
"""

from json import load


def get_config_object() -> dict:
  """
  Return a dictionary with the
  configuration of the server.
  """

  # getting
  OBJECT = load(open('./config.json'))
  return OBJECT

