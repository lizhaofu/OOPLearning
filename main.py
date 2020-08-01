#!/usr/bin/env python3.7
# -*- coding: UTF-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2020/7/26 18:24
# @File    : main.py
# @Software: PyCharm
"""
from animal import Animal
from bird import Bird
from cat import Cat
from manager import Manager

# cat = Animal("加菲猫", 8)
# # bees = [Animal('bee' + str(i), 5) for i in range(1000)]
# print(cat)
# # print(cat.cprop)
# # cat.color = "grap"
# # print(hasattr(cat, 'color'))
#
# xiaoming = Manager(cat)
#
# print(xiaoming.recordTime())
# print(xiaoming.getFeedingTime())

jiafeimao = Cat("加菲猫", 8, 'gray', 'CatGerre')
print(jiafeimao)


if __name__ == "__main__":
    jiafeimao = Cat('jiafeimao',2,'gray','CatGenre')
    haiying = Bird('haiying',40,'blue','BirdGenre')

    Manager(jiafeimao).recordTime()
    print('#'*30)
    Manager(haiying).recordTime()
