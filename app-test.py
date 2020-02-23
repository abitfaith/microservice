import os
from flask import Flask
from redis import Redis

os.system('mknod -m 644 /dev/urandom c 1 9')
app = Flask(__name__)
redis = Redis(host='192.168.20.2', port=6379)

@app.route('/')
def hello():
	redis.incr('hits')
	return 'HelloWorld! I have been seen %s times.' % redis.get('hits')
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
