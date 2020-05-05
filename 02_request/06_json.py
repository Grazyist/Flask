#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: request
 @ File   : 05_response.py
 @ Author : Cheng
 @ Data   : 2020/4/30 14:34
 @ Desc   : 返回信息的处理
"""
from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/index")
def index():
    # json就是字符串,通过json.dumps方法可以把字典转化为字符串,json.loads把字符串转化为字典
    data = {
        "name": "grist",
        "age": 18
    }
    # json_str = json.dumps(data)
    # return json_str, 200, {"Content-Type": "application/json"}
    # jsonify 帮助转化为json数据，并设置响应头Content-Type为application/json
    # return jsonify(data)
    return jsonify(city="sc",
                   county="china")
if __name__ == '__main__':
    app.run(debug=True)
