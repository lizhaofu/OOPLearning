#!/usr/bin/env python3.7
# -*- coding: UTF-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2020/7/26 18:53
# @File    : cat.py
# @Software: PyCharm
"""
from animal import Animal


class Cat(Animal):

    # __slots__ = ('color', 'genre', "name", "speed")

    def __init__(self, name, speed, color, genre):
        super().__init__(name, speed)
        self.color = color
        self.genre = genre

    # 重写方法
    def getSpeedBehavior(self):
        print('running speed of %s is %s' % (self.name, self._speed))
        return self._speed

