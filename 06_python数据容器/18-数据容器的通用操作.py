"""
# 数据容器通用操作：遍历规则
1. for循环：列表、元组、字符串、集合、字典，全部5种容器都支持for遍历。
2. while循环：依靠下标实现遍历
   ✅ 支持while：列表、元组、字符串（有序、有下标索引）
   ❌ 不支持while：集合、字典（无序，无下标索引，无法用下标取值）

总结：所有容器都能for循环；只有序列类型可以while循环遍历。
"""
from builtins import max

# 定义五大容器
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# 通用函数1：len() 统计容器内元素总个数
print(f"列表 元素个数有: {len(my_list)}")
print(f"元组 元素个数有: {len(my_tuple)}")
print(f"字符串元素个数有: {len(my_str)}")
print(f"集合 元素个数有: {len(my_set)}")
print(f"字典 元素个数有: {len(my_dict)}")

# 通用函数2：max() 获取容器最大值
print(f"列表 最大的元素是: {max(my_list)}")
print(f"元组 最大的元素是: {max(my_tuple)}")
print(f"字符串最大的元素是: {max(my_str)}")
print(f"集合 最大的元素是: {max(my_set)}")
print(f"字典 最大的元素是: {max(my_dict)}")

# 通用函数3：min() 获取容器最小值
print(f"列表 最小的元素是: {min(my_list)}")
print(f"元组 最小的元素是: {min(my_tuple)}")
print(f"字符串最小的元素是: {min(my_str)}")
print(f"集合 最小的元素是: {min(my_set)}")
print(f"字典 最小的元素是: {min(my_dict)}")

# 通用类型转换
# list(容器)：其他容器转为列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")

# tuple(容器)：其他容器转为元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"元组转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组结果是：{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是：{tuple(my_dict)}")

# str(容器):其他容器转为字符串
print(f"列表转字符串的结果是：{str(my_list)}")
print(f"元组转字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串结果是：{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}")

# set(容器)：其他容器转为集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合结果是：{set(my_str)}")
print(f"集合转集合的结果是：{set(my_set)}")
print(f"字典转集合的结果是：{set(my_dict)}")

# 进行容器的排序sorte()   排序完之后以列表的容器形式输出
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "bdce fga"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 1, "key1": 2, "key2": 3, "key5": 4, "key4": 5}

print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")

# 反向排序 reverse=True
print(f"列表对象的反向排序结果：{sorted(my_list, reverse=True)}")
print(f"元组对象的反向排序结果：{sorted(my_tuple, reverse=True)}")
print(f"字符串对象反向的排序结果：{sorted(my_str, reverse=True)}")
print(f"集合对象的反向排序结果：{sorted(my_set, reverse=True)}")
print(f"字典对象的反向排序结果：{sorted(my_dict, reverse=True)}")
# dict转换有特殊限制，不能直接把列表/元组/字符串转字典

# 容器通用功能总览
# | 功能                          | 描述                                       |
# | ----------------------------- | ------------------------------------------ |
# | 通用for循环                   | 遍历容器（字典是遍历key）                  |
# | max                           | 容器内最大元素                             |
# | min()                         | 容器内最小元素                             |
# | len()                         | 容器元素个数                               |
# | list()                        | 转换为列表                                 |
# | tuple()                       | 转换为元组                                 |
# | str()                         | 转换为字符串                               |
# | set()                         | 转换为集合                                 |
# | sorted(序列, [reverse=True])  | 排序，reverse=True表示降序，返回有序列表    |