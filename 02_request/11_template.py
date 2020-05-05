
#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: request
 @ File   : 08_session.py
 @ Author : Cheng
 @ Data   : 2020/4/30 16:40
 @ Desc   : Jinja2 模板
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
def index():
    data = {
        "name": "python1",
        "age": 12,
        "my_dict": {"city": "sc"},
        "my_list": [1, 2, 3, 4, 5, 6],
        "my_int":0
    }
    # return render_template("index.html", name="python", age=18)
    return render_template("index.html", **data)


# 自定义过滤器
# 方法一
def list_step_2(li):
    return li[::2]

# 注册过滤器            代码行为，函数   名字
app.add_template_filter(list_step_2, "li2")

# 方法二
@app.template_filter("li3")
def list_step_3(li):
    return li[::3]

if __name__ == '__main__':
    app.run(debug=True)



