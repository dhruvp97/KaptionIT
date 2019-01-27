import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

class getWebEntities: 
    def __init__(self, fileName):
        self.fileName = fileName 

    # Web Entities Results
    def detect_web(self, option):
        # The name of the image file to annotate
        path = self.fileName 

        file_name = os.path.join(
            os.path.dirname(__file__),
            self.fileName)

        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.web_detection(image=image)
        annotations = response.web_detection

        if option == 'Best guess label': 
            if annotations.best_guess_labels:
                for label in annotations.best_guess_labels:
                    #print('\nBest guess label: {}'.format(label.label))
                    return label.label
                    

        if option == 'Find web entities': 
            bestEntity = ' '
            if annotations.web_entities:
                #print('\n{} Web entities found: '.format(
                #    len(annotations.web_entities)))

                bestEntity = annotations.web_entities[0].description

            #for entity in annotations.web_entities:
            #    if entity.score > highScore
                #print('\n\tScore      : {}'.format(entity.score))
                #print(u'\tDescription: {}'.format(entity.description))
            return bestEntity
