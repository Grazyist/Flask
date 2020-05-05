#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: flask
 @ File   : convert_demo.py
 @ Author : Cheng
 @ Data   : 2020/4/26 22:46
 @ Desc   :
"""
from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

# 创建flask类的应用对象
# __name__表示为当前模块的名字，
#             模块名，flask以当前模块所在的目录为根目录,m默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)     # 入路径，寻找静态目录与模板目录位置的参数

# 转换器
# 127.0.0.1:5000/goods/123

# @app.route("/goods/<int:goods_id>")
@app.route("/goods/<goods_id>")     # 不加转换器，默认是字符串规则（除/的任意字符）
def goods_detail(goods_id):
    """ 定义视图函数"""
    return "goods detail page %s" % goods_id

# 1、定义自己的转换器
# 手机号转换器
class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super(MobileConverter, self).__init__(url_map)
        self.regex = r'1[34578]\d{9}'

# 万能转换器
class RegexConverter(BaseConverter):
    """"""
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会去使用这个属性进行路由的正则匹配
        self.regex = regex
    def to_python(self, value):      # 接收参数，可以进行数据过滤
        """"""
        print("to_python方法被调用")
        # return "invoking to_python function"
        # value是在路径进行正则表达式匹配的时候提取的参数
        return value

    def to_url(self, value):
        """使用url_for的方法可以调用"""
        print("url 方法被调用")
        # return "15111111111"
        return value

# 2、将自定义的转换器添加到flask中
app.url_map.converters["re"] = RegexConverter
app.url_map.converters["mobile"] =MobileConverter

# 127.0.0.1:5000/send/15103454654
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send_sms(mobile):
    return "send sms to %s" % mobile

@app.route("/index")
def index():
    # /send/15103858309
    url = url_for("send_sms", mobile="15103858309")
    return redirect(url)


@app.route("/call/<re(r''):tel>")
def call_tel(tel):
    pass

# @app.route("/send/<mobile:mobile_num>")
# def send_sms(mobile_num):
#     return "send sms to %s" % mobile_num

if __name__ =='__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    #   启动flask程序
    app.run(debug=True)