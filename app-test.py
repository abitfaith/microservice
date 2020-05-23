import os
from datetime import datetime
from flask import Flask, render_template, request
from jinja2 import Markup
import redis
import random
os.system('mknod -m 644 /dev/urandom c 1 9')
app = Flask(__name__, static_folder="templates")
@app.route('/insert')
def insert():
	a = datetime.now()
	temp = 1
	while temp < 1000:
		redis2 = redis.Redis(host='192.168.2.108', port=6379)
		tt = 0
		while tt < 20:
			redis2.set(tt, tt)
			tt = tt + 1
		temp = temp +1
	b = datetime.now()
	print((b-a).seconds)
	return str((b-a).seconds)
	
@app.route('/')
def hello():
	return render_template("test.html")
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
