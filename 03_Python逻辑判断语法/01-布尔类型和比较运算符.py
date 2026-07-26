# 布尔类型的字面量 true表示真 false表示假
"""
Python六大常用数据类型
| 大类 | 细分类型 | 整体描述 | 详细说明&示例 |
| ---- | ---- | ---- | ---- |
| 数字（Number） | int、float、complex、bool | 数值类数据 | int整数：10、-10；float浮点数：13.14；复数4+3j；布尔True=1、False=0 |
| 字符串（str） | 字符串 | 存储文本 | 承载所有文字、符号 |
| 列表（List） | 列表 | 有序可变 | 最常用，可增删改元素 |
| 元组（Tuple） | 元组 | 有序不可变 | 数据固定，无法修改 |
| 集合（Set） | 集合 | 无序、去重 | 自动剔除重复内容 |
| 字典（Dictionary） | 字典 | 无序键值对 | key和value一一映射 |
"""
"""
Python比较运算符汇总
| 运算符 | 描述 | 示例 |
|--------|------|------|
| == | 判断左右内容是否相等，成立返回True，不成立返回False | a=3,b=3，a == b 结果为 True |
| != | 判断左右内容是否不相等，成立返回True，不成立返回False | a=1,b=3，a != b 结果为 True |
| > | 判断左侧数值是否大于右侧，成立返回True | a=7,b=3，a > b 结果为 True |
| < | 判断左侧数值是否小于右侧，成立返回True | a=3,b=7，a < b 结果为 True |
| >= | 判断左侧是否大于或等于右侧，满足其一即为True | a=3,b=3，a >= b 结果为 True |
| <= | 判断左侧是否小于或等于右侧，满足其一即为True | a=3,b=3，a <= b 结果为 True |
"""

"""
    演示布尔类型的定义
    以及比较运算符的应用
"""

# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1},类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2},类型是：{type(bool_2)}")
# 比较运算符的使用
# ==，!=,>,<,>=,<=
# 演示进行内容的相等比较
num1 = 10
num2 = 10
print(f"10 == 10的结果是:{num1==num2}")

num1 = 10
num2 = 15
print(f"10 != 15的结果是：:{num1!=num2}")

name1 = "itcast"
name2 = "itheima"
print(f"itcast == itheima 结果是：{name1==name2}")

# 演示>,<，≧，≦的比较运算
num1 = 10
num2 = 5
print(f"10 > 5 的结果是:{num1>num2}")
print(f"10 < 5 的结果是：:{num1<num2}")

num1 = 10
num2 = 10
print(f"10 >= 10的结果是：:{num1>=num2}")
print(f"10 <= 11的结果是：:{num1<=num2}")

