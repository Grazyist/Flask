#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: 03_template
 @ File   : db_demo.py
 @ Author : Cheng
 @ Data   : 2020/5/3 13:42
 @ Desc   :
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    """sqlalchemy的配置参数"""
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:cheng1130@127.0.0.1:3306/db_flask'

    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建数据库sqlalchenmy哦工具对象
db = SQLAlchemy(app)


class Role(db.Model):
    """"用户角色"""
    __tablename__ = "tbl_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    users = db.relationship("User", backref="role")    # 关联的类，可以找全部

    def __repr__(self):
        """定义之后，可以让显示对象的时候更加直观"""
        return "Role object: name=%s" % self.name

# 创建数据库模型类
class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_user"  # 指明数据库的表名

    id = db.Column(db.Integer, primary_key=True)    # 整型的主键，会默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        """定义之后，可以让显示对象的时候更加直观"""
        return "User object: name=%s" % self.name


if __name__ == '__main__':
    # 清除数据库中的所有数据
    db.drop_all()

    # 创建所有的表
    db.create_all()

    # 创建对象
    role1 = Role(name="admin")


    # session记录对象任务
    db.session.add(role1)
    # 提交任务到数据库中
    db.session.commit()

    role2 = Role(name="stuff")
    db.session.add(role2)
    db.session.commit()

    us1 = User(name='Tom', email='Tom@163.com', password='123456', role_id=role1.id)
    us2 = User(name='Jim', email='Jim@163.com', password='456789', role_id=role2.id)
    us3 = User(name='Lucy', email='Lucy@126.com', password='1564515', role_id=role2.id)
    us4 = User(name='Grist', email='Grist@gmail.com', password='4564', role_id=role1.id)

    # 一次保存多条数据
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()