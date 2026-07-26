print("hello")
print("world")

# 不换行：end=''
"""
print("hello",end='')
print("world",end='')
"""

print("hello world")
print("itheima best")

# 制表符 \t
print("hello\tworld")
print("itheima\tbest")

# 通过while循环，输出九九乘法表的内容
# 1.控制行的循环 i < 9
# 2.控制每一行输出的循环 j <= i

# 定义外层循环的控制变量
i = 1
while i <= 9:

    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        # 内层循环的print语句，不要换行,通过\t制表符进行对齐
        print((f"{j} * {i} = {i * j}\t"), end='')
        j += 1

    i = i + 1
    print("\n") # print空内容，就是输出一个换行