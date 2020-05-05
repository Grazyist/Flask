#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: flask
 @ File   : 01_request.py
 @ Author : Cheng
 @ Data   : 2020/4/27 19:06
 @ Desc   :
"""
from flask import Flask, request


app = Flask(__name__)

# 接口 API11111111111111111111111
# 127.0.0.1:5000/index?city=shangcai&country=china   查询字符串  QueryString
@app.route("/index", methods=["GET","POST"])
def index():
    # request中包含了前端发送过来的所有请求数据，请求上下文seesion也是
    # form和data是用来提取请求具体数据
    # 通过request.form.get可以提取请求体中的表单格式数据，是一个类字典的对象
    # 通过get方法只能拿到多个同名参数的第一个，拿全部通过getlist存到列表中
    name = request.form.get("name")
    age = request.form.get("age")
    name_li = request.form.getlist("name")

    # 如果请求体的具体数据不是表单格式的（如json格式），可以通过request.data获取
    print("request.data: %s" % request.data)

    #args是用来提取url中的参数（查询字符串）
    city = request.args.get("city")
    return "index page  hello name=%s, age=%s, city=%s,name_li=%s" % (name, age, city, name_li)

# def register():
#     if request.method == 'GET'
#             return  render(request, "register.html")
#     else:
#



if __name__ ==  '__main__':
    app.run(debug=True)