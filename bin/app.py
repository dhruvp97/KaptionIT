import os
from flask import Flask, render_template, request
from sightengine.client import SightengineClient

app = Flask(__name__)

client = SightengineClient('{api_user}', '{api_secret}') # don't forget to add your credentials

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(filename)
    invalidImage = False

    output = client.check('nudity', 'wad', 'celebrities', 'scam', 'face-attributes').set_file(filename)

    # contains nudity
    if output['nudity']['safe'] <= output['nudity']['partial'] and output['nudity']['safe'] <= output['nudity']['raw']:
        invalidImage = True
    # contains weapon, alcohol or drugs
    if output['weapon'] > 0.2 or output['alcohol'] > 0.2 or output['drugs'] > 0.2:
        invalidImage = True
    # contains scammers
    if output['scam']['prob'] > 0.85:
        invalidImage = True
    # contains celebrities
    if 'celebrity' in output:
        if output[0]['prob'] > 0.85:
            invalidImage = True
    # contains children
    if 'attributes' in output:
        if output['attributes']['minor'] > 0.85:
            invalidImage = True

    if invalidImage:
        os.remove(filename)

    return render_template('index.html', invalidImage=invalidImage, init=True)
