# 思考：如果函数没有使用return语句返回数据，那么函数有返回值吗？
# 实际上是：有的。

# Python中有一个特殊的字面量：None，其类型是：<class 'NoneType'>
# 无返回值的函数，实际上就是返回了：None这个字面量

# None表示：空的、无实际意义的意思
# 函数返回的None，就表示，这个函数没有返回什么有意义的内容。
# 也就是返回了空的意思。

# 无return语句的函数返回值
def say_hi():
    print("你好呀")

result = say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是{type(result)}")

# 主动返回None的函数
def say_hi2():
    print("你好呀")
    return None

result = say_hi2()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是{type(result)}")

# None类型的应用场景
# None作为一个特殊的字面量，用于表示：空、无意义，其有非常多的应用场景。

# 场景1：用在函数无返回值上
# 函数不写return，默认自动返回None

# 场景2：用在if判断上
# 1. 在if判断中，None等同于False
# 2. 一般用于在函数中主动返回None，配合if判断做相关处理

# 场景3:用于声明无内容的变量上
# 1.定义变量，但暂时不需要有具体值，可以用None来代替
# 2.暂不赋予变量具体值 如：name = None

# None用于if判断
def check_age(age):
    if age > 18:
        return "Success"
    else:
        return None

result = check_age(16)
if not result:
    # 进入if表示result是None值 也就是False
    print("未成年，不可以进入")

# None用于声明无初始内容的变量
name = None

# 总结：
# 1. 什么是None
# None是类型'NoneType'的字面量，用于表示：空的、无意义的

# 2. 函数如何返回None
# - 不使用return语句即返回None
# - 主动return None

# 3. 使用场景
# - 函数返回值
# - if判断
# - 变量定义
# 以上场景都可以用None来去表示