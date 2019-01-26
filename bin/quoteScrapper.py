from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

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

def getQuote(object):
    raw_html = simple_get('https://www.brainyquote.com/search_results?q='+object)
    html = BeautifulSoup(raw_html, 'html.parser')
    for i, link in enumerate(html.select('a')):
        if link.get('title') == 'view quote':
            print(i, link.text)
