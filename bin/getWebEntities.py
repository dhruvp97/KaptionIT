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

    detect_web(fileName)

# Web Entities Results
def detect_web(path):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.web_detection(image=image)
    annotations = response.web_detection

    if annotations.best_guess_labels:
        for label in annotations.best_guess_labels:
            print('\nBest guess label: {}'.format(label.label))

    if annotations.web_entities:
        print('\n{} Web entities found: '.format(
            len(annotations.web_entities)))

        for entity in annotations.web_entities:
            print('\n\tScore      : {}'.format(entity.score))
            print(u'\tDescription: {}'.format(entity.description))

# Driver
main('resources\k2.jpg')
