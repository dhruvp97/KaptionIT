import io
import os
from bin.quoteScrapper import getQuoteSetA
from bin.quoteScrapper import getQuoteSetB
import bin.getWebEntities as webE
from bin.getNaturalLanguage import NLAnalysis

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def main(fileName): 
    w1 = webE.getWebEntities(fileName)
    bestEntity, entityScore = w1.detect_web('Find web entities')
    #bestLabel = w1.detect_web('Best guess label')
    print('Best Guessed Entity >> ' + bestEntity[0])
    quoteSetA = getQuoteSetA(bestEntity[0], 150)
    quoteSetB = getQuoteSetB(bestEntity[0], 150)
    '''
    for quote in quoteSetA:
        print(quote)
    for quote in quoteSetB: 
        print(quote)
    '''
    quoteSet = quoteSetA + quoteSetB
    q = NLAnalysis(bestEntity, entityScore, quoteSet, 5)
    for quote in q: 
        print(quote)
# Driver
main('resources/images/friends.jpg')





































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