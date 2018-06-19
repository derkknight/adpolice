import requests
import re
import time
from bs4 import BeautifulSoup

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
    score = int(len(word_list)/len(ad_text)*100)
#    return page_text, ad_text, count
    similar = True if score > 20 else False
    return word_list, len(ad_text), score, similar


print(police_ad('test_att.png', 'https://www.att.com/smallbusiness/explore/specialoffers.html'))