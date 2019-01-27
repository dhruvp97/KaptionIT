# import os
# from flask import Flask, render_template, request
#
# app = Flask(__name__, static_url_path='/static')
# fileN = '/static/image.jpg'
# UPLOAD_FOLDER = os.path.basename('static')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
# @app.route('/')
# def hello_world():
#     return render_template('index.html')
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     file = request.files['image']
#     f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     fileN = "/static/" + file.filename
#     # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
#     file.save(f)
#     caption = fileN
#     return render_template('index.html', user_image = fileN, image_text = caption)
#
# # @app.route('/index')
# # def show_index():
# #     full_filename = os.path.join(app.config['UPLOAD_FOLDER'], fileN)
# #     return render_template("index.html", user_image = full_filename)

from flask import Flask, redirect, render_template, request, session, url_for
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

import os

app = Flask(__name__)
dropzone = Dropzone(app)
# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'
# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'
app.config['SECRET_KEY'] = 'supersecretkeygoeshere'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB
@app.route('/', methods=['GET', 'POST'])
def index():

    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']
    # handle image upload from Dropzone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)

            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename
            )
            # append image urls
            file_urls.append(photos.url(filename))

        session['file_urls'] = file_urls
        return "uploading..."
    # return dropzone template on GET request
    return render_template('index.html')
@app.route('/results')
def results():
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))
    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    file_url = file_urls[0];
    session.pop('file_urls', None)

    return render_template('index.html', file_urls=file_url, image_captions)
