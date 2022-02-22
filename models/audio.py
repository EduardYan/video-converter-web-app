"""
Model to create a audio.
"""


class Audio:
  """
  Create a Audio object
  with properties name and path.
  """

  def __init__(self, name:str, path:str) -> None:
    self.name = name
    self.path = path

  def __str__(self) -> str:
      return f'This is a audio with name {self.name} and path {self.path}'