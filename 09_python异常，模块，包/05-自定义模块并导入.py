# 制作自定义模块
# Python自带很多内置模块，若需要个性化功能，可以自己制作模块，即自定义模块

# 注意：
# 任意Python文件都能作为自定义模块；模块文件名必须遵守Python标识符命名规范

# 导入自定义模块使用
import my_module1
from my_module1 import test
test(1,2)

# 导入不同模块的同名功能 执行后面的函数调用
from my_module1 import test
from my_module2 import test
test(1,2)

#   __main__变量
from my_module1 import test

#   __all__变量
from my_module1 import *
test_a(1,2)
test_b(1,2)

# 1.如何自定义模块并导入？
# 在Python代码文件中正常编写代码，使用import、from关键字，和导入内置模块的方式一致，导入后就能使用。

# 2.__main__变量功能
# if __name__ == "__main__"
# 只有文件被直接运行时，才会执行if里面的代码；
# 若该文件被别的程序导入为模块，if内代码不会执行。

# 3.注意事项
# 多个模块存在同名函数/功能，先后全部导入时，后导入的功能会覆盖先导入的同名功能。