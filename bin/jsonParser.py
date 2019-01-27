import json
import random

class jsonParser: 
    def __init__(self, fileName): 
        self.fileName = fileName 

    def extract(self, readLabel):
        setFound = False
        HttpLink = [] 
        with open(self.fileName, 'r') as jsonIn:
            data_dict = json.load(jsonIn)
            #print(data_dict)
        for label in data_dict['labels']: 
            if label['id'] == readLabel or (label['id'] == 'Extra' and setFound == False):
                setFound = True
                for link in label['caption']:
                    a = len(link)
                    if a == 1:  
                        HttpLink.append(link['link'])
                    else: 
                        for index in range (0, a): 
                            HttpLink.append(link['link'+str(index + 1)])
        return HttpLink
