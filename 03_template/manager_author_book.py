#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: Flask
 @ File   : author_book.py
 @ Author : Cheng
 @ Data   : 2020/5/4 14:38
 @ Desc   :
"""
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


class Config(object):
    """sqlalchemy的配置参数"""
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:cheng1130@127.0.0.1:3306/author_book'

    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "ubenwuihbgieog"


app.config.from_object(Config)

db = SQLAlchemy(app)

# 创建flask脚本管理工具对象
manager = Manager(app)

# 创建数据库迁移工具对象
Migrate(app, db)

# 向manager对象中添加数据库的操作指令
manager.add_command("db", MigrateCommand)


# 定义数据库的模型
class Author(db.Model):
    """作者"""
    __tablename__ = "tbl_authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    weibo = db.Column(db.String(64))
    # 反向连接
    books = db.relationship("Book", backref="author")
    qq = db.Column(db.String(64))


class Book(db.Model):
    """书籍"""
    __tablename__ = "tbl_books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.ForeignKey("tbl_authors.id"))


# 创建表单模型类，与前端打交道的

class AuthorBookForm(FlaskForm):
    """作者数据模型类"""
    author_name = StringField(label=u"作者", validators=[DataRequired(u"作者必填")])
    book_name = StringField(label=u"书籍", validators=[DataRequired(u"书籍必填")])
    submit = SubmitField(label=u"保存")



@app.route("/", methods=["GET", "POST"])
def index():
    # 创建表单对象
    form = AuthorBookForm()

    if form.validate_on_submit():
        # 验证表单成功
        # 提取表单数据
        author_name = form.author_name.data
        book_name = form.book_name.data

        # 保存数据库
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        # book = Book(name_book_name, author=author)  # 后面的author是上面的反连接
        db.session.add(book)
        db.session.commit()

    # 查询数据库n
    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li, form=form)




#
# # post方法  /delete_book   json
# # {"book_id":xxx}
# @app.route("/delete_book", methods=["POST"])
# def delete_book():
#      """删除数据的视图"""
#      # req_data = request.data
#      # json.loads(req_data)       # 接收的json转换为字典
#      # 如果前端发送的请求体数据是json格式，get_json会解析成字典的简写方式
#      # get_json要求前端传送的数据的"content-Type": "application/json"
#      req_dict = request.get_json()
#      book_id = req_dict.get("book_id")
#
#      # 删除数据
#      book = Book.query.get(book_id)
#      db.session.delete(book)
#      db.session.commit()
#
#     # jsonify不仅转化为json，而且"content-Type": "application/json"
#      return jsonify(code=0, message="OK")

# GET方法    /delete_book?book_id=xxx
@app.route("/delete_book", methods=["GET"])
def delete_book():
    """删除数据的视图"""
    book_id = request.args.get("book_id")

    # 删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == '__main__':

    # # 添加测试数据
    # db.drop_all()
    # db.create_all()
    # au_xi = Author(name='我吃西红柿')
    # au_qian = Author(name='萧潜')
    # au_san = Author(name='唐家三少')
    # db.session.add_all([au_xi, au_qian, au_san])
    # db.session.commit()
    #
    # bk_xi = Book(name='吞噬星空',author_id=au_xi.id)
    # bk_xi1 = Book(name='春芒', author_id=au_qian.id)
    # bk_qian = Book(name='缥缈之旅', author_id=au_qian.id)
    # bk_san = Book(name='冰火魔厨', author_id=au_san.id)
    # db.session.add_all([bk_xi, bk_xi1, bk_qian, bk_san])
    # db.session.commit()
    # app.run(debug=True)

    # 通过manager启动程序
    manager.run()