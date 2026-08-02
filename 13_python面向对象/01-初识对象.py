# 设计类（class）
# 创建对象
# 对象属性赋值

# 设计一个类
class Student:
    name = None    # 记录学生姓名
    gender = None  # 记录学生性别
    nationality = None # 记录学生国籍
    native_place = None # 记录学生籍贯
    age = None    # 记录学生年龄

# 创建一个对象
stu_1 = Student()
# 对象属性进行赋值
stu_1.name = "林俊杰"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.age = 31
stu_1.native_place = "山东省"
# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.age)
print(stu_1.native_place)

# 1.生活中或是程序中，都可以使用设计表格、生产表格、填写表格的形式组织数据

# 2.现实表格操作 和 程序面向对象对应关系：
# 设计表格 对应：设计类（class）
# 打印表格 对应：创建对象
# 填写表格 对应：对象属性赋值

# 整体逻辑流程：
# 先设计类（通用模板）
# 基于类可以创建对象1、对象2……对象N多个实例
# 每个对象都有属性1、属性2……属性N，给属性赋值
# 赋值等同于给每张表格填写各类信息
# 最终每个对象对应一张填写完成的表格，即打印表格1、表格2……表格N
