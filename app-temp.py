# -*- coding:utf8 -*-
import os
import random

import RPi.GPIO as GPIO

from flask import Flask, render_template, request, jsonify
from jinja2 import Markup

os.system('mknod -m 644 /dev/urandom c 1 9')
app = Flask(__name__, static_folder="templates")
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.IN)
# 页面路由
@app.route("/")
def index():
    return render_template("index2.html")

idx = -1

# 接收更新请求，读取，返回数据路由
@app.route("/lineDynamicData")
def update_line_data():
    global idx
    idx = idx + 1
    # 从温度传感器中读出温度数据
    return jsonify({"name": idx, "value": GPIO.input(19)})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
