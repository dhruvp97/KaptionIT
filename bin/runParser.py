import jsonParser as jparser

parse = jparser.jsonParser('resources/Caption.json')
parse.extract('food', 'chips')
