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
		# file name for photo
		file_name = photos.save(request.files['photo'])
		print('file name', file_name)
	else:
		return render_template("index.html", error="File wasn't uploaded.")
	if url:
		#page_data = {'url':url, 'score':5}
		page_data = police_ads.police_ad('static/img/' + file_name, url)
		#models.create_submission(url, 5)
		print(page_data)
		return render_template("results.html", page_data=page_data)
	else:
		print("no URL", url)
		return render_template("index.html", error="No URL to the company website.")

if __name__ == '__main__':
	app.run(debug=True)