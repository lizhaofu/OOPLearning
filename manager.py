#!/usr/bin/env python3.7
# -*- coding: UTF-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2020/7/26 18:34
# @File    : manager.py
# @Software: PyCharm
"""

import time

from bird import Bird
from cat import Cat


class Manager(object):
    def __init__(self, animal):
        self.animal = animal
        self.__t = time.time()

    def recordTime(self):
        print('feeding time for %s is %.0f' % (self.animal.name, self.__t))
        self.animal.getSpeedBehavior()

    def getFeedingTime(self):
        return '%0.f' % (self.__t,)
