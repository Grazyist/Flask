#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: flask
 @ File   : url_demo.py
 @ Author : Cheng
 @ Data   : 2020/4/26 21:53
 @ Desc   : 专门写路由的
"""
from flask import Flask, current_app, redirect, url_for
# import demo

# 创建flask类的应用对象
# __name__表示为当前模块的名字，
#             模块名，flask以当前模块所在的目录为根目录,m默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)     # 入路径，寻找静态目录与模板目录位置的参数


@app.route("/")
def index():
    """ 定义视图函数"""
    return 'Hello, World!'

# 通过methods限定访问方式
@app.route("/post_only",methods = ["GET", "POST"])
def post_only():
    return 'post only page'

# 同一路由装饰多个视图函数
@app.route("/hello",methods = ["POST"])
def hello():
    return 'hello 1'

@app.route("/hello",methods = ["GET"])
def hello2():
    return 'hello 2'

# 同一个视图函数对应多个路由装饰器（即路径）
@app.route('/hi1')
@app.route('/hi2')
def hi():
    return 'hi page!'

# 反向解析
@app.route("/login")
def login():
    # url = "/"    # 写死路径
    # 使用url_for的函数，通过视图函数和名字找到视图对应的url路径
    url = url_for("index")      # 视图函数名字就是路径的名字
    return redirect(url)

if __name__ =='__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    #   启动flask程序
    app.run(debug=True)