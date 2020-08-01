#!/usr/bin/env python3.7
# -*- coding: UTF-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2020/7/26 18:18
# @File    : animal.py
# @Software: PyCharm
"""


class Animal(object):

    cprop = "我是类上的属性cprop"

    def __init__(self, name, speed):
        self.name = name
        self._speed = speed

    def __str__(self):
        return '''Animal({0.name},{0._speed}) is printed
                name = {0.name}
                speed = {0._speed}'''.format(self)

    def getSpeedBehavior(self):
        pass





        # print(Animal.cprop)