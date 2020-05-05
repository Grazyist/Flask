#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: 03_template
 @ File   : 02_macro.py
 @ Author : Cheng
 @ Data   : 2020/5/2 22:19
 @ Desc   : 宏的使用方法
"""
from flask import Flask, render_template, flash


app = Flask(__name__)

# flag = True

app.config["SECRET_KEY"] = "24fafasf768jnkn"


@app.route("/")
def index():

    # 使用闪现flash!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if flag:
    #     添加闪现信息
        flash("hello1")
        flash("hello2")
        global flag
        flag = False
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
