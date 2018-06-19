import requests
import re
import time
from bs4 import BeautifulSoup


def get_text(link):
    page = requests.get('{}'.format(link), headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',})
    link = link
    soup = BeautifulSoup(page.text, 'html.parser')
    corpus = []
    corpus.append(str(soup.title.string))
    corpus.append(str(soup.find_all('p')))
    corpus.append(str(soup.find_all('h1')))
    corpus.append(str(soup.find_all('h2')))
    corpus.append(str(soup.find_all('h3')))
    corpus.append(str(soup.find_all('h4')))
    #print(len(text))
    #print(title)
    #print(text)
    
    #corpus = ''.join(corpus)
    corpus = ''.join(corpus)
    corpus = str(corpus).lower()
    corpus = re.sub('<.*?>','',corpus, flags=re.DOTALL)
    corpus = corpus.replace('[', '')
    corpus = corpus.replace(']', '')

    return corpus

print(get_text('http://shop.nhl.com/source/google-ak1900nhl?utm_campaign=NHL_Brand_USA|24482432&utm_medium=ppc&ks_id=6220_kw4164922&utm_term=nhl%20com%20shop&matchtype=e&utm_source=g&target=aud-346635865587:kwd-25784773202&pcrid=251981313802&adposition=1t1'))