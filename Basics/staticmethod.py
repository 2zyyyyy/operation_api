# @File:staticmethod.py
# @Author:2zyyyyy
# @Time:2019年03月11日
# @Explain: staticmethod 应用场景:编写类时需要采用很多不同的方式来创建实例，而我们只有一个__init__函数，此时静态方法就派上用场了
import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():  # 用Date.now()的形式去产生实例，该实例用的是当前时间
        t = time.localtime()  # 获取结构化的时间格式
        return Date(t.tm_year, t.tm_mon, t.tm_mday)  # 新建实例并返回

    @staticmethod
    def tomorrow():  # 用Date.tomorrow()的形式去产生实例，该实例用的是明天的时间
        s = 24 * 60 * 60
        t = time.localtime(time.time() + s)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


# 附加知识点__str__的用法
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '<name %s, age %s>' % (self.name, self.age)


if __name__ == '__main__':
    a = Date('1998', '1', '1')  # 自定义时间
    b = Date.now()  # 采用当前时间
    c = Date.tomorrow()  # 采用明天时间

    print(a.year, a.month, a.day)
    print(b.year, b.month, b.day)
    print(c.year, c.month, c.day)

    p1 = People('egon', 18)
    print(p1)
    str(p1)
