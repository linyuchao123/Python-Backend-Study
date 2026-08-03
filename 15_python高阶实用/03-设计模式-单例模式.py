# 单例模式
# 单例模式(Singleton Pattern)是一种常用的软件设计模式,该模式的主要目的是确保某一个类只有一个实例存在。
# 在整个系统中,某个类只能出现一个实例时,单例对象就能派上用场。
# · 定义:保证一个类只有一个实例,并提供一个访问它的全局访问点
# · 适用场景:当一个类只能有一个实例,而客户可以从一个众所周知的访问点访问它时。

# 单例的实现模式：
# ===== test.py 文件 =====
# class StrTools:
#     pass
#
# str_tool = StrTools()

# ===== 其他文件 =====
# from test import str_tool
#
# s1 = str_tool
# s2 = str_tool
# print(s1)
# print(s2)
# s1和s2是同一个对象