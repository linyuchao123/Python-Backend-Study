# 魔术方法介绍
# 之前学的__init__构造方法，属于Python类自带的内置方法
# Python内置、自带特殊功能的类方法统称为魔术方法

# 常见魔术方法清单：
# __init__：构造方法，创建对象自动执行
# __str__：字符串方法，自定义对象打印输出内容
# __lt__：用于大于、小于符号（> <）的对象比较
# __le__：用于大于等于、小于等于符号（>= <=）的对象比较
# __eq__：用于双等号 == 判断两个对象是否相等

# 补充：魔术方法数量很多，日常掌握常用的几种就足够使用

# __str__ 字符串方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # __str__魔术方法: 字符串自由输出
    def __str__(self):
        return f"Student类对象，name： {self.name} age：{self.age}"

    # __lt__魔术方法：  用于小于大于比较
    def __lt__(self,other):
        return self.age < other.age

    # __le__魔术方法:  用于小于等于和大于等于的比较
    def __le__(self,other):
        return self.age <= other.age

    # __eq__魔术方法:  用于比较运算符比较
    def __eq__(self,other):
        return self.name == other.name and self.age == other.age


stu1 = Student("周杰伦",31)
stu2 = Student("林俊杰",36)
print(stu1)
print(str(stu2))
print(stu1 < stu2)
print(stu1 > stu2)
print(stu1 <= stu2)
print(stu1 >= stu2)
print(stu1 != stu2)
print(stu1 == stu2)

# __lt__ 小于符号比较方法 大于也可以比较
# __le__ 小于等于比较方法
# __eq__ 比较运算符实现方法
