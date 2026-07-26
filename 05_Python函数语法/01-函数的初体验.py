# 函数：是组织好的，可重复使用的，用来实现特定功能的代码段
# 需求：统计字符串的长度，不使用内置函数len（）
str1 = "itheima"
str2 = "itcast"
str3 = "python"

# 定义一个计数的变量
count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是：{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}的长度是：{count}")

count = 0
for i in str3:
    count += 1
print(f"字符串{str3}的长度是：{count}")

# 可以使用函数，来优化这个过程
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

my_len(str1)
my_len(str2)
my_len(str3)

"""
函数知识点总结
1. 函数定义：
函数是组织好的、可重复使用的、用来实现特定功能的代码段

2. 使用函数的好处：
① 将功能封装在函数内，可供随时随地重复利用
② 提高代码的复用性，减少重复代码，提高开发效率
"""