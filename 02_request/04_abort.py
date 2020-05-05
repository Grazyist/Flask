#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: request
 @ File   : 04_abort.py
 @ Author : Cheng
 @ Data   : 2020/4/27 22:59
 @ Desc   :
"""

from flask import Flask, request, abort, Response


app = Flask(__name__)


@app.route('/login', methods=["GET"])
def login():
    # name = request.for.get()
    # pwd = request.for.get()
    name = ""
    pwd = ""
    if name != "zhangshan" or pwd != "admin":
        #  使用abort函数可以立即终止视图函数的执行
        #  并可以返回前端特定的信息
        #  1、传递状态码信息，必须是标准的http状态码
        abort(404)
        # 传递响应体信息
        # resp = Response("login failed")
        # abort(resp)
    return "login success"

# 定义错误处理的方法
@app.errorhandler(404)
def handle_404_error(err):
    """自定义错误处理方法"""
    # 这个函数的返回值将是前端用户看到的结果
    return "出现404错误信息，错误信息：%s" % err

if __name__ == '__main__':
    app.run(debug=True)