# 异常出现的两种结果
# 1. 程序报错直接终止运行
# 2. 提示错误信息，程序正常继续运行
# 原生代码默认是第一种，商用程序需要第二种，依靠异常捕获实现
# 异常捕获：预判报错位置，准备应对逻辑，报错后执行备用方案，保证程序不整体崩溃

# 捕获常规异常
# Python捕获常规异常基础语法：
# try:
    # 存放有可能报错、出现异常的代码
    # 可能发生错误的代码
# except:
    # 当try内部代码出现任意异常时，执行此处代码做兜底处理
    # 如果出现异常执行的代码

# 基础捕获异常语法
try:
    f = open("lyc.txt","r",encoding="utf-8")
except:
    print(f"出现异常了，因为文件不存在，我将open的模式，改为w模式去打开")
    f = open("lyc.txt","w",encoding="utf-8")

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print('出现了变量为定义的异常，name变量名称未定义错误')
    print(e)  # e表示异常信息，即报错信息
# 捕获多个异常
try:
    # print(name)
    print(1 / 0)
# 同时捕获 NameError（变量未定义）、ZeroDivisionError（除零错误）
except (NameError, ZeroDivisionError) as e:
    print('出现了变量未定义 或者 除以0的异常错误 ZeroDivision错误...')
    print(e)

#捕获所有异常
try:
    print("Hello")
except Exception as e:
    print("出现异常了")
    print(e)
else:
    print("没有异常")

# finally 不管有没有异常都输出
try:
    f = open("lyc.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现异常了")
    f = open("lyc.txt", "w", encoding="UTF-8")
else:
    print("好高兴，没有异常。")
finally:
    print("我是finally，有没有异常我都要执行")
    f.close()