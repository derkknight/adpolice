from PIL import Image
import pytesseract
import argparse
import cv2
import os


def process_image(img, blur=True, thresh=False):

    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if blur == True:
        gray = cv2.medianBlur(gray, 3)

    elif thresh == True:
	    gray = cv2.threshold(gray, 0, 255,
		    cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)

    return text

#print(process_image('http://shop.nhl.com/source/google-ak1900nhl?utm_campaign=NHL_Brand_USA|24482432&utm_medium=ppc&ks_id=6220_kw4164922&utm_term=nhl%20com%20shop&matchtype=e&utm_source=g&target=aud-346635865587:kwd-25784773202&pcrid=251981313802&adposition=1t1', 'example_02.png'))
