from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import jsonParser as jparser

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def getQuoteSetA(object, toleranceLevel):
    setA = []
    object = object.replace(' ', '+')
    count  = 0
    raw_html = simple_get('https://www.brainyquote.com/search_results?q='+ object)
    html = BeautifulSoup(raw_html, 'html.parser')
    #print('Result >>')
    for i, link in enumerate(html.select('a')):
        if link.get('title') == 'view quote':
            sizeOfText = len(link.text)
            if sizeOfText > 0 and sizeOfText < toleranceLevel:
                setA.append(link.text)
                count = count + 1
    if count == 0 and toleranceLevel < 175:
        return getQuoteSetA(object, toleranceLevel + 10)
    else:
        return setA

def getQuoteSetB(object, toleranceLevel):
    setB = []
    count = 0
    parse = jparser.jsonParser('../resources/MainCaption.json')
    HttpLinks = parse.extract(object)
    for link in HttpLinks:
        raw_html = simple_get(link)
        html = BeautifulSoup(raw_html, 'html.parser')
        for i, link in enumerate(html.select('ul' and 'li')):
            if not link.select('a'):
                sizeOfText = len(link.text)
                if sizeOfText > 0 and sizeOfText < toleranceLevel:
                    setB.append(link.text)
                    count = count + 1
    if count == 0 and toleranceLevel < 175:
        return getQuoteSetB(object, toleranceLevel + 10)
    else:
        return setB
