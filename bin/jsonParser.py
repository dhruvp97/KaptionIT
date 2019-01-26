import json
import random

class jsonParser: 
    def __init__(self, fileName): 
        self.fileName = fileName 

    def extract(self, readLabel, name):
        with open(self.fileName, 'r') as jsonIn:
            data_dict = json.load(jsonIn)
            #print(data_dict)
        for label in data_dict['labels']: 
            if label['id'] == readLabel:
                for caption in label['caption']:
                    #print('Starting Lines: ')
                    randIntS = random.randint(1,10) % len(caption['starting'])
                    randIntE = random.randint(1,10) % len(caption['ending'])
                    print(caption['starting'][randIntS]['line'] + name +
                          caption['ending'][randIntE]['line'])

                    '''
                    for startCaption in caption['starting']:
                        print(startCaption)
                    print('Ending Lines: ')
                    for endCaption in caption['ending']:
                        print(endCaption)
                    '''
