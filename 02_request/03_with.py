#!/user/bin/env python\
# -*- coding: utf-8 -*-
"""
 @ Project: request
 @ File   : 03_with.py
 @ Author : Cheng
 @ Data   : 2020/4/27 22:19
 @ Desc   :
"""
# f = open("./1.txt", "wb")
# # 向文件内写内容
# try:
#     f.write("hello flask")
# except Exception:
#     pass
# finally:
#     # 3、关闭文件
#     f.close()

# 上下文管理器

# with open("./1.txt", "w") as f:
#     f.write('hello falsk1')
#     f.write('hello falsk2')
#


class Foo(object):

    def __enter__(self):
        """进入with语句的时候被with调用"""
        print("enter called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with语句的时候被with调用"""
        print("exit callled")
        print("exc_type:%s" % exc_type)
        print("exc_val:%s" % exc_val)
        print("exc_tb:%s" % exc_tb)


#    对象
with Foo() as foo:
    print("hello python")
    a = 1/0
    print("hello end")
