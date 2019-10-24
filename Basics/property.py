# @File:property.py
# @Author:2zyyyyy
# @Time:2019年03月08日
# @Explain: 特性（property）property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值

import math


class Circle:
    def __init__(self, radius):  # 圆的半径radius
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2  # 计算面积

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius  # 计算周长


c = Circle(10)
print(c.radius)
# 可以像访问数据属性一样去访问area 会触发一个函数的执行 动态计算出一个值
print(c.area)
print(c.perimeter)
# 注意：此时的特性area和perimeter不能被赋值
c.area = 3
