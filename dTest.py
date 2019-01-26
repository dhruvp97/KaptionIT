import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources/k2.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)

response = client.web_detection(image=image)
annotations = response.web_detection

if annotations.best_guess_labels:
    for label in annotations.best_guess_labels:
        print('\nBest guess label: {}'.format(label.label))

if annotations.pages_with_matching_images:
    print('\n{} Pages with matching images found:'.format(
        len(annotations.pages_with_matching_images)))

    for page in annotations.pages_with_matching_images:
        print('\n\tPage url   : {}'.format(page.url))

        if page.full_matching_images:
            print('\t{} Full Matches found: '.format(
                   len(page.full_matching_images)))

            for image in page.full_matching_images:
                print('\t\tImage url  : {}'.format(image.url))

        if page.partial_matching_images:
            print('\t{} Partial Matches found: '.format(
                   len(page.partial_matching_images)))

            for image in page.partial_matching_images:
                print('\t\tImage url  : {}'.format(image.url))

if annotations.web_entities:
    print('\n{} Web entities found: '.format(
        len(annotations.web_entities)))

    for entity in annotations.web_entities:
        print('\n\tScore      : {}'.format(entity.score))
        print(u'\tDescription: {}'.format(entity.description))

if annotations.visually_similar_images:
    print('\n{} visually similar images found:\n'.format(
        len(annotations.visually_similar_images)))

    for image in annotations.visually_similar_images:
        print('\tImage url    : {}'.format(image.url))
