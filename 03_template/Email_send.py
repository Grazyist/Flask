#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: Flask
 @ File   : Email_send.py
 @ Author : Cheng
 @ Data   : 2020/5/5 17:40
 @ Desc   :Flask-Mail 通过python内置的smtplib包，可以用在Flask程序中发送邮件
Flask-Mail连接到简单邮件协议（Simple Mail Transfer Protocol,SMTP）服务器，并把邮件交给服务器发送
"""
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# 配置邮箱：服务器/端口/传输层安全协议/邮箱名/密码
app.config.update(
    DRBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='1091291085@qq.com',
    MAIL_PASSWORD='galuixlimbodjgcj',
)

mail = Mail(app)    # 此乃对象，亦为工具


@app.route('/')
def index():
    # sender发送方，recipients接收方列表
    #                  标题
    msg = Message("This is a test", sender='1091291085@qq.com', recipients=['15103858309@163.com'])
    # 邮件内容
    msg.body = "Flask test mail"
    # 发送邮件
    mail.send(msg)
    print("mail send.... ")
    return "send succeed"


if __name__ == "__main__":
    app.run()
