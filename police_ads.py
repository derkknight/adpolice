import re
import time
from bs4 import BeautifulSoup
from pprint import pprint

from scrape import get_text
from img_text import process_image

def police_ad(ad_name, url):
    page_text = get_text(url)
    ad_text = process_image(ad_name)
    ad_text = ad_text.split()
    count = 0
    word_list = []
    for word in ad_text:
        if word.lower() in page_text:
            count += 1
            word_list.append(word)
    score = int(float(len(word_list))/len(ad_text)*100)
    print(float(len(word_list))/len(ad_text))
    similar = True if score > 20 else False
    return ad_text, word_list, score, similar, url


# pprint(police_ad('static/img/betterment.png', 'https://www.betterment.com/start-investing/?utm_campaign=ProspectingDontJustInvest2018&utm_medium=display&utm_source=Prospecting&offer_campaign_id=11494573-13d0-4721-87ca-d796a40ccbc3'))