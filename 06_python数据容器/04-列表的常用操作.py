# 列表的常用操作（方法）
# 列表除了可以：
# 1. 定义
# 2. 使用下标索引获取值
# 以外，列表也提供了一系列功能：
# 插入元素
# 删除元素
# 清空列表
# 修改元素
# 统计元素个数
# 等等功能，这些功能我们都称之为：列表的方法

# 列表的查询功能（方法）
# 回忆：函数是一个封装的代码单元，可以提供特定功能。
# 在Python中，如果将函数定义为class（类）的成员，那么函数会称之为：方法
#
# # 普通函数
# def add(x, y):
#     return x + y
#
# # 类中的方法
# class Student:
#     def add(self, x, y):
#         return x + y
#
# 方法和函数功能一样，有传入参数，有返回值，只是方法的使用格式不同：
# 函数的使用：num = add(1, 2)
# 方法的使用：student = Student()
#            num = student.add(1, 2)

mylist = ['itcast', 'itheima', 'python']

# 1.1查找某元素在列表内的下标索引
index = mylist.index('itheima')
print(f"itheima在列表中的下标索引值是：{index}")

# 1.2如果被查找的元素不存在，会报错
# index = mylist.index('hello')
# print(f"hello在列表中的下标索引值是：{index}")

# 列表的修改功能（方法）
# 修改特定位置（索引）的元素值：
# 语法：列表[下标] = 值
# 可以使用如上语法，直接对指定下标（正向、反向下标均可）的值进行：重新赋值（修改）

# 正向下标
my_list = [1, 2, 3]
my_list[0] = 5
print(my_list)  # 结果：[5, 2, 3]

# 反向下标
my_list = [1, 2, 3]
my_list[-3] = 5
print(my_list)  # 结果：[5, 2, 3]

# 2.修改特定下标索引的值
mylist[0] = "传智教育"
print(f"列表被修改元素后，结果是：{mylist}")

# 3.在指定位置下标位置插入新元素
# 插入insert语法：insert(下标，元素),在指定的下标位置，插入指定的元素
mylist.insert(1,"best")
print(f"列表插入元素，结果是：{mylist}")

# 4.在列表的尾部追加‘’‘单个’‘’新元素
# 追加append语法：列表.append（元素）
mylist.append("黑马程序员")
print(f"列表在追加了元素后，结果是：{mylist}")

# 5.在列表的尾部追加’‘’一批‘’‘新元素
# 列表.ectend(其他数据容器） 将其他数据容器的内容取出，依次添加到列表尾部
my_list2 = [1,2,3]
mylist.extend(my_list2)
print(f"列表在追加了一个新的列表后,结果是：{mylist}")

# 6.删除指定下标索引的元素（2种方式）
mylist = ['itcast', 'itheima', 'python']

# 6.1 方式1:del 列表[下标]
del mylist[2]
print(f"列表删除元素后结果是：{mylist}")

# 6.2 方式2:列表.pop(下标)
mylist = ['itcast', 'itheima', 'python']
element = mylist.pop(2)
print(f"通过pop方法取出元素后列表内容：{mylist},取出的元素是：{element}")

# 7.删除元素在列表中的第一个匹配值
# 语法：列表.remove（元素）
mylist = ['itcast', 'itheima', 'itcast','itheima','python']
mylist.remove("python")
print(f"通过remove方法移除元素后，列表的结果是:{mylist}")

# 8.清空列表
# 列表.clear
mylist.clear()
print(f"列表被清空了，结果是:{mylist}")

# 9.统计列表内某元素的数量
# 语法：列表.count(数量)
mylist = ['itcast', 'itheima', 'itcast','itheima','python']
count = mylist.count('itheima')
print(f"列表中itheima的数量是：{count}")

# 10.统计列表中全部的元素数量
mylist = ['itcast', 'itheima', 'itcast','itheima','python']
count = len(mylist)
print(f"列表的元素数量总共有：{count}个")

"""
列表的方法 - 总览
┌────┬──────────────────────┬─────────────────────────────────────┐
│编号 │ 使用方式              │ 作用                                │
├────┼──────────────────────┼─────────────────────────────────────┤
│ 1  │ 列表.append(元素)     │ 向列表中追加一个元素                │
│ 2  │ 列表.extend(容器)     │ 将数据容器的内容依次取出，追加到列表尾部 │
│ 3  │ 列表.insert(下标,元素) │ 在指定下标处，插入指定的元素        │
│ 4  │ del 列表[下标]        │ 删除列表指定下标元素                │
│ 5  │ 列表.pop(下标)        │ 删除列表指定下标元素                │
│ 6  │ 列表.remove(元素)     │ 从前向后，删除此元素第一个匹配项    │
│ 7  │ 列表.clear()         │ 清空列表                            │
│ 8  │ 列表.count(元素)      │ 统计此元素在列表中出现的次数        │
│ 9  │ 列表.index(元素)      │ 查找指定元素下标，找不到报错ValueError │
│ 10 │ len(列表)             │ 统计容器内有多少元素                │
└────┴──────────────────────┴─────────────────────────────────────┘
"""
# 列表的特点总结
# 1. 可以容纳多个元素（上限为2**63-1、9223372036854775807个）
# 2. 可以容纳不同类型的元素（混搭）
# 3. 数据是有序存储的（有下标序号）
# 4. 允许重复数据存在
# 5. 可以修改（增加或删除元素等）