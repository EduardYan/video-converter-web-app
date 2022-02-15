"""
This file have the routes
to use in the server.
"""


import os
from flask import Blueprint, flash, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename
from helpers.config import CONFIG
from helpers.utils import get_videos_files
from models.video import Video
from moviepy.editor import VideoFileClip

# routes
converter = Blueprint('converter', __name__)

@converter.route('/')
def initial():
  """
  Initial route
  for the server.
  """

  # getting the videos list to show
  videos_list = get_videos_files()

  return render_template('index.html', videos_list = videos_list)

@converter.route('/uploader', methods = ['POST'])
def uploader():
  if request.method == 'POST':
    
    try:
      f = request.files['video-file']
      filename = secure_filename(f.filename)
      video = Video(filename)
      f.save(os.path.join(CONFIG['UPLOAD_FOLDER'], video.filename))

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

  video_name = request.form['video-name']
  upload_folder = CONFIG['UPLOAD_FOLDER']

  video_mp4 = VideoFileClip(upload_folder + video_name)
  audio_mp3 = video_mp4.audio

  to_save_audio = f'/files/audios/{video_name}.mp3'
  audio_mp3.write_audiofile(to_save_audio) 

  return send_file(to_save_audio)


@converter.route('/about')
def about():
  """
  Route for render the about page.
  """

  return render_template('about.html')