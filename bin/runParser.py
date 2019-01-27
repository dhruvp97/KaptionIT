import jsonParser as jparser

parse = jparser.jsonParser('resources/MainCaption.json')
HttpLinks = parse.extract('friend')
print(HttpLinks)
