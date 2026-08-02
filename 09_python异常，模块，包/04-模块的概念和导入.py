# 什么是模块
# Python模块（Module），是一个Python文件，以.py结尾。模块能定义函数，类和变量，模块里也能包含可执行的代码

# 模块的作用：python中有很多各种不同的模块，每一个模块都可以帮助我们快速的实现一些功能，比如实现和时间相关的功能就可以使用time模块
# 我们可以认为一个模块就是一个工具包，每一个工具包中都有各种不同的工具供我们使用进而实现各种不同的功能.

# 大白话：模块就是一个Python文件，里面有类、函数、变量等，我们可以拿过来用（导入模块去使用）

# 模块的导入方式
# 模块在使用前需要先导入 导入的语法如下:
# [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]

# 常用的组合形式如下：
# import 模块名
# from 模块名 import 类、变量、方法等
# from 模块名 import *
# import 模块名 as 别名
# from 模块名 import 功能名 as 别名

# import模块名
# 基本语法：
# import 模块名
# import 模块名1, 模块名2

# 调用格式：模块名.功能名()
# 使用import导入time模块使用sleep功能(函数）
import time # 导入python内置的time模块（time.py这个代码文件）
print("你好")
time.sleep(5)  #通过.可以使用模块内部的全部功能(类，函数，变量)
print("我好")

# 通用导入语法格式：[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]

# from 模块名 import 功能名
# 基本语法：
# from 模块名 import 功能名
# 调用方式：功能名()

# 使用from导入time的sleep功能（函数）
from time import sleep
print("你好")
sleep(5)
print("我也好")

# 使用 * 导入time模块的全部功能
from time import *   # * 表示全部的意思
print("你好")
sleep(5)
print("我也好")

# 使用as给特定功能加上别名
import time as t
print("你好")
t.sleep(5)
print("我也好")

from time import sleep as sl
print("你好")
sl(5)
print("我也好")

# 总结：
# 1.什么是模块？
# 模块就是一个Python代码文件，内含类、函数、变量等，我们可以导入进行使用。

# 2.如何导入模块
# 通用语法：[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]

# 3.注意事项：
# from可以省略，直接import即可
# as别名可以省略
# 通过"."来确定层级关系
# 模块的导入一般写在代码文件的开头位置