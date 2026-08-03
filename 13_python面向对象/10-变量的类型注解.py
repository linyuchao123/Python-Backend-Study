# 类型注解
# Python在3.5版本的时候引入了类型注解，以方便静态类型检查工具，IDE等第三方工具。
# 类型注解：在代码中涉及数据交互的地方，提供数据类型的注解（显式的说明）。
# 主要功能：
# · 帮助第三方IDE工具（如PyCharm）对代码进行类型推断，协助做代码提示
# · 帮助开发者自身对变量进行类型注释
import random

import json
from importlib.metadata import pass_none

# 支持：
# · 变量的类型注解
# · 函数（方法）形参列表和返回值的类型注解

# 类型注解的语法：
# 为变量设置类型注解
# 基础语法：变量: 类型

# 基础数据类型注解
var_1: int = 10
var_2: float = 3.1415926
var_3: bool = True
var_4: str = "itheima"

# 类对象类型注解
class Student:
    pass

stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"itheima": 666}
my_str: str = "itheima"

# 容器类型详细注解
my_list1: list[int] = [1, 2, 3]
my_tuple2: tuple[str, int, bool] = ("itheima", 666, True)
my_set3: set[int] = {1, 2, 3}
my_dict4: dict[str, int] = {"itheima": 666}

# 注意:
# · 元组类型设置类型详细注解，需要将每一个元素都标记出来
# · 字典类型设置类型详细注解，需要2个类型，第一个是key第二个是value

# 除了使用 变量: 类型，这种语法做注解外，也可以在注释中进行类型注解。
# 在注释中进行类型注解
# 语法：
# # type: 类型

# 在注释中进行类型注解
class Student:
    pass

var_11 = random.randint(1, 10)  # type: int
var_22 = json.loads('{"name":"zhangsan"}')       # type: dict[str, str]
def func():
    return 10
var_33 = func()   # type:int

# 类型注解的限制
var_4 :int = "itheima"
var_5:str = 123

# 类型注解的语法
# 为变量设置注解，显示的变量定义，一般无需注解：
var_1: int = 10
var_2: list = [1, 2, 3]
var_3: dict = {"itheima": 666}
var_4: Student = Student()
# 如图，就算不写注解，也明确的知晓变量的类型

class Student:
    pass

# 一般，无法直接看出变量类型之时会添加变量的类型注解
var_1: int = random.randint(1, 10)
var_2: dict = json.loads(('{"name":"zhangsan"}'))
var_3: Student = func()

# 1.什么是类型注解，有什么作用？
# 在代码中涉及数据交互之时，对数据类型进行显式的说明，可以帮助：
# · PyCharm等开发工具对代码做类型推断协助做代码提示
# · 开发者自身做类型的备注

# 2.类型注解支持：
# · 变量的类型注解
# · 函数（方法）的形参和返回值的类型注解

# 3.变量的类型注解语法
# · 语法1：变量: 类型
# · 语法2：在注释中，# type: 类型

# 4.注意事项
# · 类型注解只是提示性的，并非决定性的。数据类型和注解类型无法对应也不会导致错误
