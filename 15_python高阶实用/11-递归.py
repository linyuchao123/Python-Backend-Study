# ========== 1. 什么是递归 ==========
# 递归：在满足限定条件时，函数内部调用自身的编程技巧

# ========== 2. 递归编写注意事项 ==========
# ① 必须设置退出条件，否则会出现无限递归，程序报错
# ② 做好返回值传递，保证内层函数结果可以逐层向外层传递

# ========== 3. os模块常用三个方法 ==========
# os.listdir(路径)：列出指定目录下所有文件、文件夹的名称列表
# os.path.isdir(路径)：判断对应路径是否为文件夹，是返回True，否返回False
# os.path.exists(路径)：判断对应路径是否真实存在，存在返回True，不存在返回False

import os

# listdir示例：获取目录内内容
file_list = os.listdir("./test_dir")

# isdir示例：判断是否为文件夹
res_dir = os.path.isdir("./test_dir/demo")

# exists示例：判断路径是否存在
res_exist = os.path.exists("./test_dir")