#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: request
 @ File   : 08_session.py
 @ Author : Cheng
 @ Data   : 2020/4/30 16:40
 @ Desc   :
"""
from flask import Flask
from flask_script import Manager    # 启动命令的管理类


app = Flask(__name__)

# 创建Manger管理类的对象
manager = Manager(app)

@app.route("/index")
def index():
    return "index page"


if __name__ == '__main__':
    # app.run(debug=True)
    # 通过管理对象来启动flask
    manager.run()

