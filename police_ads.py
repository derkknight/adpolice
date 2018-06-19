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
#    return page_text, ad_text, count
    return word_list


print(police_ad('test.png', 'http://shop.nhl.com/source/google-ak1900nhl?utm_campaign=NHL_Brand_USA|24482432&utm_medium=ppc&ks_id=6220_kw4164922&utm_term=nhl%20com%20shop&matchtype=e&utm_source=g&target=aud-346635865587:kwd-25784773202&pcrid=251981313802&adposition=1t1'))