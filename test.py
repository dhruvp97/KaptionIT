import io
import os
from bin.quoteScrapper import getQuote
import bin.getWebEntities as webE

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def main(fileName): 
    w1 = webE.getWebEntities(fileName)
    bestEntity = w1.detect_web('Find web entities')
    #bestLabel = w1.detect_web('Best guess label')
    print('Best Guessed Entity >> ' + bestEntity)
    getQuote(bestEntity, 150) 

# Driver
main('resources/images/sunset.jpg')





































'''
def main(fileName):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        fileName)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    response2 = client.web_detection(image=image)
    annotations = response.web_detection

    print('Labels:')
    for label in labels:
        print(label.description)

    detect_web(fileName)
'''