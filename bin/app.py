import os
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')
fileN = '/static/image.jpg'
UPLOAD_FOLDER = os.path.basename('static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    fileN = "/static/" + file.filename
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)
    caption = fileN
    return render_template('index.html', user_image = fileN, image_text = caption)

# @app.route('/index')
# def show_index():
#     full_filename = os.path.join(app.config['UPLOAD_FOLDER'], fileN)
#     return render_template("index.html", user_image = full_filename)
