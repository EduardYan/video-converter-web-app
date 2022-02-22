"""
This file have the routes
to use in the server.
"""


from flask import (
  Blueprint,
  flash,
  render_template,
  request,
  redirect,
  send_file,
  url_for
)
from helpers.config import CONFIG
from helpers.utils import get_videos_files, convert_to_audio, delete_file, save_file

# routes
converter = Blueprint('converter', __name__)

# to upload the files
upload_folder = CONFIG['UPLOAD_FOLDER']


@converter.route('/')
def initial():
  """
  Initial route
  for the server.
  """

  # getting the videos list to show
  videos_list = get_videos_files()

  # returning the page with the video list to show
  return render_template('index.html', videos_list = videos_list)


@converter.route('/uploader', methods = ['POST'])
def uploader():
  if request.method == 'POST':
    
    try:
      # getting the video file and saving
      file = request.files['video-file']
      save_file(file)

      # showing message in case the file is save sucessfulyy
      flash('File Upload Succesfully.')

    except:
      flash('Some problem with upload the file. Verify the file, please.')

    return redirect(url_for('converter.initial'))


@converter.route('/convert', methods = ['POST'])
def convert():
  """
  Route for convert the video
  to audio.
  """

  # getting the file to convert
  video_name = request.form['video-name']

  try:
    # converting to a audio
    new_audio = convert_to_audio(upload_folder, video_name)

    # passing to the page the new audio to download
    return render_template('download.html', audio_file = new_audio)

  except:
    flash('Some Problem to convert the file to audio.')
    return redirect(url_for('converter.initial'))


@converter.route('/delete/<video_name>')
def delete(video_name):
  """
  Route for delete a file
  in the server to convert.
  """

  try:
    # delete the video file and audio file and redirect to initial page
    delete_file(upload_folder, video_name)

    flash('Video Delete Sucessfully.')

    return redirect(url_for('converter.initial'))

  # some problem is controled
  except:
    flash('Some problem to delete the file.')
    return redirect(url_for('converter.initial'))


@converter.route('/about')
def about():
  """
  Route for render the about page.
  """

  return render_template('about.html')