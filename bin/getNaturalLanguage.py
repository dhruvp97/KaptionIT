# Imports the Google Cloud client library
import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def NLAnalysis(bestEntity, entityScore, quoteSet): 
    # Instantiates a client
    client = language.LanguageServiceClient()

    score = []
    for quote in quoteSet: 
        # The text to analyze
        #print(quote)
        totalScore = 0
        
        for entity in bestEntity: 
            if entity in quote: 
                totalScore = totalScore + (1/len(quote.split()))
            #print(totalScore)
        
        text = quote
        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')
        
        # Instantiates a plain text document.
        
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        entities = client.analyze_entities(document).entities

        for entity in entities:
            #print(entity.name)
            if entity.name in bestEntity: 
                totalScore = totalScore + entity.salience 

            #entity_type = enums.Entity.Type(entity.type)
            #print('=' * 20)
            #print(u'{:<16}: {}'.format('name', entity.name))
            #print(u'{:<16}: {}'.format('type', entity_type.name))
            #print(u'{:<16}: {}'.format('salience', entity.salience))
            #print(u'{:<16}: {}'.format('wikipedia_url',
            #   entity.metadata.get('wikipedia_url', '-')))
            #print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))
        
        print(totalScore)
        score.append(totalScore)
    return score    