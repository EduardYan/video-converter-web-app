#!/usr/bin/env python3

"""
Principal file for execute the server.
"""


from app import app
from helpers.config import get_config_object


# getting the configuration
CONFIG = get_config_object()


if __name__ == '__main__':
  # running with configuration
  app.run(port = CONFIG['PORT'], host = '0.0.0.0', debug = True)