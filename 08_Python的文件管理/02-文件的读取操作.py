# 文件：文本文件 音频文件 视频文件 可执行文件 图像文件
# 打开文件-->读写文件-->关闭文件
# Python open() 文件打开函数
# 作用：打开已有文件，或创建全新文件
# 语法格式：open(name, mode, encoding)
import time
from fileinput import close

# 参数详解
# name：字符串类型，目标文件名，可附带完整文件路径
# mode：文件打开访问模式，可选只读、写入、追加等模式
# encoding：文件编码格式，推荐统一使用 UTF-8

# 示例代码
f = open('python.txt', 'r', encoding="UTF-8")
# 补充说明：encoding不在第三位，不能用位置传参，必须用关键字参数指定

# 注意事项
# 变量 f 是open返回的文件对象，属于Python特殊数据类型，自带属性与方法
# 后续可通过 对象.属性 / 对象.方法 操作文件，面向对象阶段详细讲解

# open函数mode三大基础访问模式详解
# 模式r：只读模式
# 1. 只能读取文件，不能写入修改
# 2. 文件指针默认在文件开头
# 3. open默认模式；文件不存在会直接报错

# 模式w：只写模式
# 1. 仅支持写入，不可读取
# 2. 文件存在：清空全部原有内容，从头写入新内容
# 3. 文件不存在：自动新建空白文件

# 模式a：追加模式
# 1. 只可写入，不可读取
# 2. 文件存在：指针在文件末尾，新内容追加到原有内容最后，不会覆盖旧文字
# 3. 文件不存在：自动创建新文件写入

# 打开文件
f = open("python.txt", "r", encoding="utf-8")
print(type(f))

# 文件读取常用方法：read()、readlines()
# read 读取文件
print(f"读取10个字节的结果:{f.read(10)}")
print(f"read方法读取全部内容的结果是:{f.read()}")
# 读取文件全部行，并分装到列表中--readlines()
lines = f.readlines()
print(f"lines对象的类型：{type(lines)}")
print(f"lines对象的内容是:{lines}")

# 1. read() 用法：文件对象.read(num)
# num：可选参数，代表读取字节长度
# 不传num：一次性读取文件全部内容
# 传入num：只读取指定字节数量的内容

# 2. readlines() 用法：文件对象.readlines()
# 一次性按行读取整个文件，返回列表
# 文件每一行内容单独作为列表的一个元素，自带换行符 \n

# 读取文件：readline
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行数据是:{line1}")
print(f"第二行数据是:{line2}")
print(f"第三行数据是:{line3}")

# for循环读取文件行
for line in f:
    print(f"每一行数据是:{line}")

# 文件的关闭 close()
f = close()
time.sleep(500000)

# with open 语法操作文件
with open("python.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"每一行数据是:{line}")

time.sleep(500000)

# Python文件读取操作汇总表格
# -------------------------------------------------------------------------------------------
# 操作语法                          | 功能说明
# -------------------------------------------------------------------------------------------
# 文件对象 = open(file, mode, encoding) | 打开文件获得文件操作对象；file文件路径，mode读写模式，encoding编码格式
# 文件对象.read(num)                   | 读取指定字节长度内容；不传num读取文件全部内容
# 文件对象.readline()                  | 一次仅读取文件一行内容
# 文件对象.readlines()                 | 一次性读取全部行，返回列表，每行作为列表元素
# for line in 文件对象                 | for循环遍历文件，单次循环获取一行数据，适配大文件
# 文件对象.close()                     | 手动关闭文件，释放资源，解除文件占用
# with open() as f                     | 上下文打开文件，代码块结束自动关闭文件，不用手动close
# -------------------------------------------------------------------------------------------
