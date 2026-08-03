# 使用Union类型，必须先导包 from typing import Union
from typing import Union

my_list: list[int] = [1, 2, 3]
my_dict: dict[str, int] = {"age": 11, "num": 3}

# 列表同时包含int和str，字典值同时包含int和str，使用Union联合类型
my_list1: list[Union[str, int]] = [1, 2, "itheima", "itcast"]
my_dict1: dict[str, Union[str, int]] = {"name": "周杰伦", "age": 31}

# 使用Union[类型, ……, 类型]
# 可以定义联合类型注解

from typing import Union

# Union联合类型注解，在变量注解、函数（方法）形参和返回值注解中，均可使用。
my_list2: list[Union[int, str]] = [1, 2, "itcast", "itheima"]
my_dict2: dict[str, Union[str, int]] = {"name": "周杰伦", "age": 31}

def func(data: Union[int, str]) -> Union[int, str]:
    pass

func()