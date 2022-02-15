"""
Utils functions to use
in the server.
"""

import os
from helpers.config import CONFIG
from models.video import Video

def get_videos_files() -> list:
  """
  Return a list with
  the files uploaded
  for convert.
  """

  videos_list = os.listdir(CONFIG['UPLOAD_FOLDER'])
  new_videos_list = [] # to save the objects

  for filename in videos_list:
    video = Video(filename)
    new_videos_list.append(video)


  del videos_list # not use

  return new_videos_list