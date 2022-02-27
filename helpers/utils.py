"""
Utils functions to use
in the server.
"""

import os

from pkg_resources import WorkingSet
from helpers.config import CONFIG
from models.video import Video
from models.audio import Audio
from moviepy.editor import VideoFileClip
from werkzeug.utils import secure_filename
from models.video import Video


# here for save new audios
# getting the working directory
WORKING_DIRECTORY = os.getcwd()
ROUTE_FOR_AUDIOS =  WORKING_DIRECTORY + CONFIG['AUDIOS_FOLDER']
RELATIVE_ROUTE_FOR_AUDIOS = '/static/files/audios/'
ROUTE_FOR_VIDEOS = WORKING_DIRECTORY + CONFIG['UPLOAD_FOLDER_VIDEOS']


def create_directories_to_save():
  """
  Create the directory for save
  the videos and for save the new audios.

  Ignore if the directories exists.

  """

  try:

    # creating the two directories of the configuration file
    os.makedirs(WORKING_DIRECTORY + '/static/files', exist_ok = True)
    os.makedirs(ROUTE_FOR_VIDEOS, exist_ok = True)
    os.makedirs(ROUTE_FOR_AUDIOS, exist_ok = True)

  except:
    print('Some problem to create the directories, verify the path.')


def get_videos_files() -> list:
  """
  Return a list with
  the files uploaded
  for convert.
  """

  try:
    videos_list = os.listdir(ROUTE_FOR_VIDEOS)
    new_videos_list = [] # to save the objects

    for filename in videos_list:
      last_extension = filename.split('.')[1]
      # only return mp4 files
      if last_extension == 'mp4':
        video = Video(filename)
        new_videos_list.append(video)

    del videos_list # not use

    return new_videos_list

  except FileNotFoundError:
    # in case the directories is not created
    create_directories_to_save()


def get_file_without_extension(path_file) -> str:
  """
  Return the path
  of the file without your extension.
  """

  file_without_extension = ''

  for word in path_file.split('.'):
    # not add the extension
    if word != 'mp4':
      # adding the new word
      file_without_extension += word
    del word

  return file_without_extension


def save_file(file) -> None:
  """
  Save the file
  passed for parameter.
  """

  # saving the file
  filename = secure_filename(file.filename)

  # validating the filename
  if filename.split('.')[1] != 'mp4':
    return False


  # in case is valid the video file
  video = Video(filename)
  file.save(
    os.path.join(ROUTE_FOR_VIDEOS, video.filename
    ))

  return True


def convert_to_audio(upload_folder:str, video_name:str) -> Audio:
  """
  Convert and save the video
  file in the audio.

  Pass the upload_folder for concact
  with the video_name parameters.

  """

  video_without_extension = get_file_without_extension(video_name)

  video_mp4 = VideoFileClip(
    WORKING_DIRECTORY + upload_folder + video_name
  )
  # getting only the audio
  audio_mp3 = video_mp4.audio
  audio = Audio(
    name = video_without_extension + '.mp3',
    path = ROUTE_FOR_AUDIOS + video_without_extension + '.mp3',
    relative_path = RELATIVE_ROUTE_FOR_AUDIOS + video_without_extension + '.mp3'
  )

  # concact to save
  to_save_audio = audio.path
  audio_mp3.write_audiofile(to_save_audio) 

  # return the audio object
  return audio


def delete_file(upload_folder:str, video_name:str) -> None:
  """
  Delete a video concact
  the folder and the video name
  passed for parameter.
  """

  # deleting the video file and the audio
  os.remove(
    WORKING_DIRECTORY + upload_folder + video_name
    )

  # getting the audio name to delete
  audio_name = get_file_without_extension(video_name)

  # in case the file to delete not yet convert to audil
  try:
    os.remove(ROUTE_FOR_AUDIOS + audio_name + '.mp3')
  except FileNotFoundError:
    pass