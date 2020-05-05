#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: 03_template
 @ File   : 01_wtf.py
 @ Author : Cheng
 @ Data   : 2020/5/2 19:39
 @ Desc   :
"""
from flask import Flask, render_template, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
import request

app = Flask(__name__)

app.config["SECRET_KEY"] = "afsaregadfgrfhsafvg32"
# 定义表单的模型类
class RegisterForm(FlaskForm):
    """自定义的注册表单模型类"""
    #                           名字          验证器
    # DAtaRequired 保证数据必须填写， 并且不能为空
    user_name = StringField(label=u"用户名", validators=[DataRequired("用户名不能为空")])
    password = PasswordField(label=u"密码", validators=[DataRequired("密码不能为空")])
    password2 = PasswordField(label=u"确认密码", validators=[DataRequired("确认密码不能为空"),
                                                         EqualTo("password", "两次密码不一致")])
    submit = SubmitField(label="提交")


@app.route("/register", methods=["GET", "POST"])
def register():

    # 创建表单对象，如果是post请求，前端发送了数据，flask会把数据构造到form对象的时候，纯放到对象中
    form = RegisterForm()

    # 判断form中的数据是否合理
    # 如果合理满足所有的验证器，则返回为真，否者返回假
    if form.validate_on_submit():
        #   表示验证合格
        #    提取数据
        uname = form.user_name.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(uname, pwd, pwd2)
        session["user_name"] = uname
        return redirect(url_for("index"))
    else:
        if request.method == 'POST':
            flash(u'信息输入有误，请重新输入！')
    return render_template("register.html", form=form)


@app.route("/index")
def index():
    user_name = session.get("user_name", "")
    return "hello %s" % user_name


if __name__ == '__main__':
    app.run(debug=True)
