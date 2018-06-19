import os
from flask import Flask, request, redirect, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES
import models

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
	if 'photo' in request.files:
		# file name for photo
		filename = photos.save(request.files['photo'])
		print('file name', filename)
	else:
		print('file not found')
		return render_template("index.html", error="Invalid Submission")
	if models.create_submission(url, 5):
		page_data = {'url':url, 'score':5}
		print(page_data)
		return render_template("results.html", page_data=page_data)
	else:
		print("no URL")
		return render_template("index.html", error="Invalid Submission")

if __name__ == '__main__':
	app.run(debug=True)