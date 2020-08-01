#!/usr/bin/env python3.7
# -*- coding: UTF-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2020/8/1 13:23
# @File    : student.py
# @Software: PyCharm
"""


class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def set_name(self,val):
        self.name = val
        return self

    def set_age(self,age):
        self.age = age
        return self

    def print_info(self):
        print("name: "+self.name)
        print("age: "+ str(self.age))
        return self

s = Student('xiaoming',100) # 创建新的实例

(
    s
    .set_name('xiaoming1')
    .set_age(25)
    .print_info()
)


# s = Student('xiaoming',100) # 创建新的实例
# s.score=10