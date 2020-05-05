#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: request
 @ File   : 02_upload.py
 @ Author : Cheng
 @ Data   : 2020/4/27 21:24
 @ Desc   :
"""

from flask import Flask, request


app = Flask(__name__)

@app.route('/upload', methods=["POST"])
def upload():
    """接收前端传过来的文件"""
    file_obj = request.files.get("pic")
    if file_obj is None:
        # 表示没有发送文件
        return "未上传文件"
    # 将文件保存到本地
    # 1、创建一个文件
    # f = open("./demo.png", "wb")
    # # 向文件内写内容
    # data = file_obj.read()
    # f.write(data)
    # # 3、关闭文件
    # f.close()
    # return "上传成功"

    # 直接使用上传的文件对象保存
    file_obj.save(".demo1.png")
    return "上传成功"

if __name__ == '__main__':
    app.run(debug=True)