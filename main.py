# -*- coding: utf-8 -*-
#！/usr/bin/python

from flask import Flask, render_template, Response, jsonify, request

# start flask app
app = Flask(__name__)


@app.route('/')
def index():
	"""Video streaming home page."""
	return render_template('index.html')


if __name__ == "__main__":
	# open and run simulink model threading
	'''
	t= threading.Thread(target=run_simulink)
	t.setDaemon(True)
	t.start()
	'''	
	# open url
	#webbrowser.open("https://127.0.0.1:5000")
	# open web service
	app.run()
