# -*- coding:utf8 -*-
import random

from flask import Flask, render_template, request, jsonify
from jinja2 import Markup

os.system('mknod -m 644 /dev/urandom c 1 9')
app = Flask(__name__, static_folder="templates")

# 页面路由
@app.route("/")
def index():
    return render_template("index.html")

idx = -1

# 接收更新请求，读取，返回数据路由
@app.route("/lineDynamicData")
def update_line_data():
    global idx
    idx = idx + 1
    # 返回的是随机数，格式不变，更改数据库中的value值
    return jsonify({"name": idx, "value": random.randrange(10, 30)})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
