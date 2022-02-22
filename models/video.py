"""
This module have the model
for a video.
"""


class Video:
  """
  Create a video object
  with a filename to use.
  """

  def __init__(self, filename:str) -> None:
    # values
    self.filename = filename
      

  def __str__(self) -> str:
      return f'This is a video object with filename {self.filename}'