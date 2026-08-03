# 函数（方法）的类型注解 - 形参注解
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray


def func(data):
    # data.app
    pass

# 如图所示:
# · 在编写函数（方法），使用形参data的时候，工具没有任何提示
# · 在调用函数（方法），传入参数的时候，工具无法提示参数类型
# 这些都是因为，我们在定义函数（方法）的时候，没有给形参进行注解

# 函数和方法的形参类型注解语法：
# def 函数方法名(形参名: 类型, 形参名: 类型, ......):
#     pass

# 对形参进行类型注解
def add(x: int, y: int):
    return x + y
add(4,5)
print("x + y = ", add(4,5))
# 函数（方法）的类型注解 - 返回值注解
# 同时，函数（方法）的返回值也是可以添加类型注解的。
# 语法如下：
# def 函数方法名(形参: 类型, ......, 形参: 类型) -> 返回值类型:
#     pass

# 对返回值进行类型注解
def func(data: list) -> list:
    pass

print(func(1))