# 什么是Python包
# 从物理上看，包就是一个文件夹，在该文件夹下包含了一个 __init__.py 文件，该文件夹可用于包含多个模块文件
# 从逻辑上看，包的本质依然是模块

# 目录结构说明：文件夹存放my_module1、my_module2、my_module3、my_module4、my_module5、my_module6多个模块，搭配__init__.py，整体成为Package包

# 包的作用：
# 当我们的模块文件越来越多时，包可以帮助我们管理这些模块，包的作用就是包含多个模块，但包的本质依然是模块

# 创建一个包
# 导入自定义的包中的模块，并使用
import my_package.my_module1
import my_package.my_module2

my_package.my_module1.info_print1()
my_package.my_module2.info_print2()

from my_package import my_module1
from my_package import my_module2
my_module1.info_print1()
my_module2.info_print2()

from my_package.my_module1 import info_print1
from my_package.my_module2 import info_print2
info_print1()
info_print2()

# 通过__all__变量，控制import
from my_package import *
my_module1.info_print1()
my_module2.info_print2()

# 自定义python包总结：
# 1.什么是Python的包？
# 包就是一个文件夹，里面可以存放许多Python的模块（代码文件），通过包，在逻辑上将一批模块归为一类，方便使用。

# 2.__init__.py文件的作用？
# 创建包会默认自动创建的文件，通过这个文件来表示一个文件夹是Python的包，而非普通的文件夹。

# 3.__all__变量的作用？
# 和模块内的作用一致，专门控制使用 import * 时可以导入哪些内容