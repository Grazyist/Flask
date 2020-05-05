#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: request
 @ File   : 07_cookie.py
 @ Author : Cheng
 @ Data   : 2020/4/30 15:25
 @ Desc   :
"""
from flask import Flask, make_response,request

app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    # 设置cookie,默认有效期临时cookie,浏览器关闭即失效
    resp.set_cookie("name", "value")
    resp.set_cookie("itcast", "python")
    # 通过max_age设置有效期，单位：秒
    resp.set_cookie("itcast1", "python1", max_age=3600)
    # 实际上是加在头上了，故可以利用下面的方法直接加头上
    resp.headers["Set_Cookie"] = "itcast2=python2; Expires=Thu, 30-Apr-2020 08:47:14 GMT; Max-Age=3600; Path=/"
    return resp

@app.route("/get_cookie")
def get_cookie():
    c = request.cookies.get("itcast")
    return c

@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("delete cookie")
    # 删除cookie,只能让它立马过期
    resp.delete_cookie("itcast1")
    return resp





if __name__ == '__main__':
    app.run(debug=True)
