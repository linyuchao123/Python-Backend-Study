# 练习案例：自定义工具包

# 1. 创建自定义包，包名：my_utils
# 2. 包内包含两个模块文件

# ----------------str_util.py 字符串工具模块----------------
# 函数 str_reverse(s)：接收字符串，返回反转后的字符串
# 函数 substr(s, x, y)：根据下标x、y对字符串做切片截取

# ----------------file_util.py 文件处理工具模块----------------
# 函数 print_file_info(file_name)
# 接收文件路径，打印文件全部内容；文件不存在捕获异常并提示；finally保证关闭文件

# 函数 append_to_file(file_name, data)
# 接收文件路径和数据，把数据追加写入文件

# 整体完成包搭建后，外部代码导入my_utils包，调用里面工具函数测试使用
"""
my_utils/              # 自定义包文件夹
├── __init__.py        # 包必备标识文件
├── str_util.py        # 字符串工具模块
└── file_util.py       # 文件操作工具模块
"""
import my_utils
# 创建my_utils 包，在包内创建：str_util.py 和 file_util.py 2个模块，并提供相应的函数

# import my_utils.str_util
from my_utils import str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("itheima",0,4))

file_util.append_to_file("test_append.txt","itheima")
file_util.print_file_info("test_append.txt")