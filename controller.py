import os
from flask import Flask, request, redirect, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES
import models
import police_ads

app = Flask(__name__) # create the application instance :)
app.secret_key = os.urandom(24)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/', methods=["GET"])
def show_home():
	return render_template("index.html", error="")

@app.route('/results', methods=["POST"])
def review(post_id=None):
	url = request.form.get('website_url')
	print('url', url)
	print("Hello")
	print(request.files)
	file_name = ""
	if 'photo' in request.files:
		file_name = photos.save(request.files['photo'])
		print('file name', file_name)
	else:
		return render_template("index.html", error="File wasn't uploaded.")
	if url:
		page_data = police_ads.police_ad('static/img/' + file_name, url)
		print(page_data)
		return render_template("results.html", page_data=page_data)
	else:
		print("no URL", url)
		return render_template("index.html", error="No URL to the company website.")

@app.route('/ads', methods=["GET"])
def show_ads(item_id=None, action=None):
	page_data = {}
	if item_id and action:
		page_data['context'] = models.get_items(item_id, action)
		return page_data
	else:
		page_data['page_num'] = 0
		page_data['need_previous'] = False
		page_data['context'] = models.get_items()
		return render_template("ads.html", page_data=page_data)

@app.route('/next/<item_id>/<page_num>', methods=["GET"])
def next_5(item_id=None, page_num=None):
	page_data = show_home(item_id, 'next')
	page_data['page_num'] = int(page_num) + 1
	page_data['need_previous'] = True
	return render_template("index.html", page_data=page_data)

@app.route('/last/<item_id>/<page_num>', methods=["GET"])
def last_5(item_id=None, page_num=None):
	page_data = show_home(item_id, 'last')
	page_data['page_num'] = int(page_num) - 1
	if page_data['page_num'] == 0:
		page_data['need_previous'] = False
	else:
		page_data['need_previous'] = True
	return render_template("index.html", page_data=page_data)

if __name__ == '__main__':
	app.run(debug=True)