import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def main(fileName):
    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        fileName)

    detect_label(fileName)

# Label Results
def detect_label(path):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)

# Driver
main('resources\k2.jpg')
