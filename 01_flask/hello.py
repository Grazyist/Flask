#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: flask
 @ File   : hello.py
 @ Author : Cheng
 @ Data   : 2020/4/26 20:09
 @ Desc   :
"""
from flask import Flask, current_app
# import demo

# 创建flask类的应用对象
# __name__表示为当前模块的名字，
#             模块名，flask以当前模块所在的目录为根目录,m默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__,      # 入路径，寻找静态目录与模板目录位置的参数
            static_url_path="/python",    # 访问静态资源的url前缀
            static_folder="static",         # 静态目录的路径，默认就是static
            template_folder="templates",    # 默认静态模板的目录就是templates
            )
# app = Flask("__main__")
# app = Flask("asdfASD")

# 配置参数使用方式
# 1、使用配置文件
# app.config.from_pyfile("config.cfg")

# 2、使用对象配置参数
class Config(object):
    DEBUG = True
    ITCAST = "python"
app.config.from_object(Config)

# # 3、直接操作config字典对象
# app.config["DEBUG"] = True


#  使用 route() 装饰器来把函数绑定到 URL:
@app.route('/')
def index():
    """ 定义视图函数"""
    # a = 1 / 0

    # 读取配置参数
    # 1、直接从全局对象app的config字典中取值
    # print(app.config.get("ITCAST"))
    # 2、通过current_app获取参数
    print(current_app.config.get("ITCAST"))


    return 'Hello, World!'

if __name__ =='__main__':
    #   启动flask程序
    app.run(host="0.0.0.0", port=5000, debug=True)