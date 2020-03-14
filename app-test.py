import os
from flask import Flask, render_template, request
from jinja2 import Markup
import redis
import random

os.system('mknod -m 644 /dev/urandom c 1 9')
app = Flask(__name__, static_folder="templates")
redis0 = redis.Redis(host='192.168.20.3', port=6379)
redis1 = redis.Redis(host='192.168.20.4', port=6379)
testnumber = 0

@app.route('/insert')
def insert():
	number = random.randint(0, 1)
	global testnumber
	temp = testnumber + 5
	
	if number == 0:
		try:
			while testnumber < temp :
				redis0.set(testnumber,testnumber)
				testnumber += 1
			return "redis0"
		except redis.exceptions.ConnectionError as e:
			while testnumber < temp :
				redis1.set(testnumber,testnumber)
				testnumber += 1
			return "redis1"
	else :
		try:
			while testnumber < temp :
				redis1.set(testnumber,testnumber)
				testnumber += 1
			return "redis1"
		except redis.exceptions.ConnectionError as e:
			while testnumber < temp :
				redis0.set(testnumber,testnumber)
				testnumber += 1
			return "redis0"

	
@app.route('/')
def hello():
	return render_template("test.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
