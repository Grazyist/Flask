#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: request
 @ File   : 05_response.py
 @ Author : Cheng
 @ Data   : 2020/4/30 14:34
 @ Desc   : 返回信息的处理
"""
from flask import Flask, request, abort, Response, make_response

app = Flask(__name__)


@app.route("/index")
def index():
    # 1、使用元组，返回自定义的响应信息
    #           响应体          状态码   响应头
    # return "index page_response", 400, [("Itcast", "python"),("City", "shangcai")]
    # return "index page_response", 400, {"Itcast": "python", "City1": "sc1"}
    # return "index page_response", "666 Itcast status", {"Itcast": "python", "City1": "sc1"}     # 只定义状态码
    # return "index page_response", "666 Itcast status"

    # 2、使用make_response 来构造响应信息
    resp = make_response("index page 2")
    resp.status = "999 state code message"  # 设置状态码
    resp.headers["city"] = "sc"     # 设置响应头
    return resp

if __name__ == '__main__':

    app.run(debug=True)