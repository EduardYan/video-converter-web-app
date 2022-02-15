"""
This module have the model
for a video.
"""


class Video:
  """
  Create a video object
  with a filename.
  """

  def __init__(self, filename:str) -> None:
    # values
    self.filename = filename
      