
import os
from flask import Flask, request, redirect, render_template
import models

app = Flask(__name__) # create the application instance :)
app.secret_key = os.urandom(24)

@app.route('/', methods=["GET"])
def show_home():
	return render_template("index.html", error="")

@app.route('/results', methods=["POST"])
def edit(post_id=None):
	url = request.form.get('url')
	if models.create_submission(url, 5):
		page_data = {'url':url, 'score':5}
		return render_template("results.html", page_data=page_data)
	else:
		return render_template("index.html", error="Invalid Submission")

if __name__ == '__main__':
	app.run(debug=True)