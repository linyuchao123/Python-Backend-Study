# 需求：列表元素借助集合实现去重
# 原始列表
# my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']

# 步骤1：定义空集合，空集合必须用set()创建，不能用{}
# empty_set = set()

# 步骤2：使用for循环遍历整个列表，逐个取出列表里的每一个元素
# for item in my_list:

# 步骤3：循环内部调用add方法，把遍历拿到的元素添加进空集合
#         集合自带自动去重特性，重复元素添加无效
#     empty_set.add(item)

# 步骤4：循环结束后，集合内全部为不重复元素，打印最终集合
# print(empty_set)

# 整体逻辑：列表循环逐个入集合，依靠集合不可重复完成信息去重
# 最终打印去重完成的集合，集合无序，输出顺序不固定

my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客',
           'itheima', 'itcast', 'itheima', 'itcast', 'best']

# 定义一个空集合
my_set = set()

# 通过for循环遍历列表
for element in my_list:
    # 在for循环中将列表的元素添加至集合
    my_set.add(element)

# 最终得到元素去重后的集合对象，并打印输出
print(f"列表的内容是: {my_list}")
print(f"通过for循环后，得到的集合对象是: {my_set}")



