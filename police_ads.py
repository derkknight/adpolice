import re
import time
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

from scrape import get_text
from img_text import process_image

stop_words = set(stopwords.words('english'))

def police_ad(ad_name, url):
    page_text = get_text(url)
    ad_text = process_image(ad_name)
    ad_text = ad_text.split()
    word_list = []
    for word in ad_text:
        for char in word:
            if not char.isalpha():
                word = word.replace(char, '')
        if word.lower() in stop_words:
            ad_text.remove(word)
        if word.lower().isalpha() and word.lower() in page_text:
            word_list.append(word)

    score = int(len(word_list)/len(ad_text)*100) if len(ad_text) > 0 else 0

    similar = True if score > 20 else False
    return ad_text, word_list, score, similar, url


text, list, score, similar, url = police_ad('test_betterment.png', 'https://www.betterment.com/start-investing/?utm_campaign=ProspectingDontJustInvest2018&utm_medium=display&utm_source=Prospecting&offer_campaign_id=11494573-13d0-4721-87ca-d796a40ccbc3')
print('Words: ', list, '\n\n', 'Score: ', score, '%\n', 'Malware!' if similar == False else '', '\n\n', 'URL: ', url)

#text, list, score, similar, url = police_ad('centrum_test.png', 'https://www.centrum.com/centrum-multigummies?ps-open&utm_campaign=%ebuy!&utm_term=%epid!&utm_content=%ecid!&utid=display&dclid=CNfx573L4NsCFQa_swod7pEHNw')
#print('Words: ', list, '\n\n', 'Score: ', score, '%\n', 'Malware!' if similar == False else '', '\n\n', 'URL: ', url)
