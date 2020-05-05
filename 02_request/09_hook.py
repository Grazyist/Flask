#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: request
 @ File   : 08_session.py
 @ Author : Cheng
 @ Data   : 2020/4/30 16:40
 @ Desc   :
"""
from flask import Flask, request, url_for

app = Flask(__name__)


@app.route("/index")
def index():
    a = 1/0
    print("index 被执行")
    return "index page"


@app.route("/hello")
def hello():
    print("hello 被执行")
    return "hello page"


@app.before_first_request
def handle_before_first_request():
    # 在第一次请求处理前先被执行
    print("handle_before_first_request 被执行")


@app.before_request
def handle_before_request():
    # 在每次请求处理前都被执行
    print("handle_before_request 被执行")

@app.after_request
def handle_after_request(response):
    # 在每次请求（视图函数处理）之后被执行，前提是视图函数没有出现异常
    print("handle_after_request 被执行")
    return response


@app.teardown_request
def handle_teardown_request(response):
    # 只运行在生产模式，调试模式下不起作用
    # 在每次请求（视图函数处理）之后都被执行，无论视图函数是否出现异常，都被执行
    path = request.path
    if path == url_for("index"):
    # if path in [url_for("index"), url_for()]:
        print("在请求钩子中判断请求的视图逻辑：index")
    elif path == url_for("hello"):
        print("在请求钩子中判断请求的视图逻辑：hello")
    print("handle_teardown_request 被执行")
    return response


if __name__ == '__main__':
    app.run(debug=False)
