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
import abc


class Animal(object):

    cprop = "我是类上的属性cprop"

    # __slots__ = ('name', '_speed')

    def __init__(self, name, speed):
        self.name = name  # 动物名字
        self._speed = speed  # 动物行走或飞行速度

    def __str__(self):
        return '''Animal({0.name},{0._speed}) is printed
                name = {0.name}
                speed = {0._speed}'''.format(self)

    # 使用abstractmethod装饰器后，变为抽象方法
    @abc.abstractmethod
    def getSpeedBehavior(self):
        pass

    # 使用装饰器的时候，需要注意：
    # 1. 装饰器名，函数名需要一直(_speed与属性名一致，可以直接传参数)
    # 2. property需要先声明，再写setter，顺序不能倒过来
    # 3. 是因为内部的self._speed1属性名和def _speed的名称必须不同，
    # 否则会导致一直在循环, 装饰器的最大循环次数默认是999


    # 读
    @property
    def _speed(self):
        return self._speed1

    # 写
    @_speed.setter
    def _speed(self, val):
        if val < 0:
            raise ValueError('speed value is negative')
        self._speed1 = val





