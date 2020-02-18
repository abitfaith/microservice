import random

from flask import Flask, render_template, request, jsonify
from jinja2 import Markup


from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line

app = Flask(__name__, static_folder="templates")

from pyecharts.charts import Line

def line_base() -> Line:
    line = (
        Line()
        .add_xaxis(["{}".format(i) for i in range(10)])
        .add_yaxis(
            series_name="",
            y_axis=[random.randrange(10, 30) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="温度数据"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line

# 页面路由
@app.route("/")
def index():
    return render_template("index.html")

# 图表路由
@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()

idx = 9

# 接收更新请求，读取，返回数据路由
@app.route("/lineDynamicData")
def update_line_data():
    global idx
    idx = idx + 1
    # 返回的是随机数，格式不变，更改数据库中的value值
    return jsonify({"name": idx, "value": random.randrange(10, 30)})


if __name__ == "__main__":
    app.run()
