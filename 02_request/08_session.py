#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: request
 @ File   : 08_session.py
 @ Author : Cheng
 @ Data   : 2020/4/30 16:40
 @ Desc   :
"""
from flask import Flask, session

app = Flask(__name__)

# flask的session需要用到的密钥字符串
app.config["SECRET_KEY"] = "adsdafdsfsdfaf223"


@app.route("/login")
def login():
    # 设置session数据
    session["name"] = "python"
    session["mobile"] = "151038587309"
    return "login success"


@app.route("/index")
def index():
    # 获取session数据
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(debug=True)
