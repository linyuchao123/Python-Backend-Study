# threading模块
# 绝大多数编程语言，都允许多线程编程，Python也不例外。
# Python的多线程可以通过threading模块来实现。

# import threading
#
# thread_obj = threading.Thread([group [, target [, name [, args [, kwargs]]]]])
# - group: 暂时无用，未来功能的预留参数
# - target: 执行的目标任务名
# - args: 以元组的方式给执行任务传参
# - kwargs: 以字典方式给执行任务传参
# - name: 线程名，一般不用设置
#
# # 启动线程，让线程开始工作
# thread_obj.start()

# 多线程编程
# 通过下方代码即可实现多线程编程
# 让一个Python程序启动2个线程，每个线程各自执行一个函数

import threading
import time

def sing():
    while True:
        print("我在唱歌，啦啦啦...")
        time.sleep(1)

def dance():
    while True:
        print("我在跳舞，哗哗哗哗哗")
        time.sleep(1)

# 创建线程对象
sing_thread = threading.Thread(target=sing)  # 创建一个唱歌的线程
dance_thread = threading.Thread(target=dance) # 创建一个跳舞的线程


# 启动线程
sing_thread.start()
dance_thread.start()

# 多线程传参
# 需要传参可以通过：
# • args参数通过元组（按参数顺序）的方式传参
# • 或使用kwargs参数用字典的形式传参

import threading
import time

def sing():
    while True:
        print("我在唱歌，啦啦啦...")
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

# 方式1：args 元组传参
sing_thread = threading.Thread(target=sing)
dance_thread = threading.Thread(target=dance, args=("我在跳舞，哈哈哈",))

# 方式2：kwargs 字典传参
# dance_thread = threading.Thread(target=dance, kwargs={"msg": "我在跳舞，哈哈哈"})

sing_thread.start()
dance_thread.start()