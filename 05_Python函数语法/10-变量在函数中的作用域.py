# 局部变量
# 变量作用域指的是变量的作用范围（变量在哪里可用，在哪里不可用）
# 主要分为两类：局部变量和全局变量
from IPython.utils.PyColorize import pride_theme


# 所谓局部变量是定义在函数体内部的变量，即只在函数体内部生效
# print(num)  # 报错：name 'num' is not defined
# 变量num定义在testA函数内部，在函数外部访问会报错

# 局部变量作用：在函数体内部临时保存数据，函数调用结束后，局部变量销毁

# 演示局部变量
def testA():
    num = 100   # num是局部变量，仅函数内可用
    print(num)

testA()
# print(num)   #test_A变量使用完之后立即销毁 num变量随之消失

# 演示全局变量(在函数内外部都可以正常使用）
num = 200

def test_a():
    print(f"test_a:{num}")

def test_b():
    print(f"test_b:{num}")

test_a()
test_b()
print(num)

# 在函数内修改全局变量
num = 200

def test_a():
    print(f"test_a:{num}")

def test_b():
    num = 500         #局部变量
    print(f"test_b:{num}")

test_a()
test_b()
print(num)

# global关键字 可以在函数内部声明变量为全局变量
num = 200

def test_a():
    print(f"test_a:{num}")

def test_b():
    global num      #设置内部定义的变量为全局变量
    num = 500         #局部变量
    print(f"test_b:{num}")

test_a()
test_b()
print(num)

# 总结：变量在函数中的作用域
# 1. 什么是局部变量
# 作用范围在函数内部，在函数外部无法使用

# 2. 什么是全局变量
# 在函数内部和外部均可使用

# 3. 如何将函数内定义的变量声明为全局变量
# 使用global关键字，语法：global 变量名