# 字符串是字符的容器，一个字符串可以存放任意数量的字符

# ========== 字符串下标（索引）知识点 ==========
# 1. 字符串支持下标访问，用法和列表、元组一致
# 正向索引：从前向后，下标从 0 开始
# 反向索引：从后向前，下标从 -1 开始

# 下标取值示例
name = "itheima"
print(name[0])   # 取第1个字符，输出 i
print(name[-1])  # 取最后一个字符，输出 a

# 2. 字符串特性：不可修改，和元组一样属于不可变容器
# 以下操作全部不允许执行，会报错：
# ① 修改下标字符：name[0] = "a"
# ② 删除字符：del name[0]、remove()、pop()
# ③ 追加字符：append()

my_str = "itheima and itcast"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}\n取下标为2的元素，值是：{value}\n取下标为-16的元素，值是：{value2}")

# my_str[2] = "H"  # 字符串无法修改
# index方法
value = my_str.index("and")
print(f"在字符串{my_str}中 查找and，其起始下标是：{value}")

# ========== 字符串替换 replace() ==========
# 语法：字符串.replace(字符串1, 字符串2)
# 功能：把原字符串中所有 字符串1 全部替换成 字符串2
# 重要关键点：字符串本身不会被改动，replace会返回全新字符串，需要用变量接收

# replace方法
new_my_str = my_str.replace("it","程序")
print(f"将字符串{my_str},进行替换后得到：{new_my_str}")

# ================== 字符串分割 split() ==================
# 语法：字符串.split(分隔符字符串)
# 功能：以指定分隔符拆分原字符串，拆分后的所有片段放进列表返回
# 重要注意：原始字符串不会被修改，最终返回的是列表类型

# split方法
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到：{my_str_list}，类型是{type(my_str_list)}")

# ==================== 字符串规整 strip() 用法 ====================
# # 用法1：strip() 不带参数，删除字符串首尾全部空格
# my_str = " itheima and itcast "
# print(my_str.strip())  # 输出：itheima and itcast
# # 原字符串不会被修改，返回新字符串
#
# # 用法2：strip("指定字符") 删除首尾所有包含在括号内的单个字符
# my_str = "12itheima and itcast21"
# print(my_str.strip("12"))  # 输出：itheima and itcast
#
# # 重要细节：传入"12"代表首尾遇见1、2任意字符都会删掉，按单个字符匹配，不是整体匹配
# # 所有字符串操作均不修改原字符串，返回新字符串，需要变量接收结果

# strip方法
my_str = "  itheima and itcast  "
new_my_str = my_str.strip()   # 不传入参数，去除首尾空格
print(f"字符串{my_str}被strip后，结果：{new_my_str}")

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip（’12）后，结果：{new_my_str}")

# 统计字符串中某个字符串的出现次数
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}it出现的次数是:{count}")

# 统计字符串的长度
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")

# ========== 字符串常用操作汇总 ==========
# 编号 | 操作                              | 说明
# --------------------------------------------------------------
# 1    | 字符串[下标]                      | 根据下标索引取出特定位置字符
# 2    | 字符串.index(字符串)             | 查找给定字符的第一个匹配项的下标
# 3    | 字符串.replace(字符串1, 字符串2) | 将字符串内全部字符串1替换为字符串2；不修改原串，返回新字符串
# 4    | 字符串.split(字符串)              | 按指定字符串分割；不修改原串，返回新列表
# 5    | 字符串.strip() / 字符串.strip(字符串) | 移除首尾空格、换行符，或首尾指定字符
# 6    | 字符串.count(字符串)              | 统计子字符串出现次数
# 7    | len(字符串)                       | 统计字符串总字符个数

"""
===================== 字符串的特点 =====================
作为数据容器，字符串有如下特点：
1. 只可以存储字符
2. 长度任意（取决于内存大小）
3. 支持下标索引
4. 允许重复字符存在
5. 不可以修改（无法增加、删除、修改内部元素）
6. 支持for循环遍历
"""