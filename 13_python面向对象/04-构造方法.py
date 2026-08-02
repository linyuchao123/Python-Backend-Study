# 构造方法介绍
# Python类中 __init__() 叫做构造方法

# 两大核心特点：
# 1. 创建类对象的一瞬间，构造方法会自动运行，不需要手动调用
# 2. 创建对象时传入的参数，会自动交给 __init__ 方法接收、使用

# 演示使用构造方法对成员变量进行赋值
# 构造方法的名称：__init__
class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print(f"Student类创建了一个类对象")

stu = Student("周杰伦",31,"18896876115")
print(stu.name)
print(stu.age)
print(stu.tel)

# 构造方法注意事项：
# 1. 构造方法固定名称为 __init__，init前后各两条下划线，不能写错下划线数量
# 2. 构造方法属于成员方法，形参第一位必须写上self，不可省略
# 3. 在构造方法中定义成员变量，必须借助self关键字

# 标准写法示例
# def __init__(self, name, age, tel):
#     self.name = name   # 将传入的name赋值给对象的成员变量name
#     self.age = age     # 将传入的age赋值给对象的成员变量age
#     self.tel = tel     # 将传入的tel赋值给对象的成员变量tel

# 原理：普通变量只属于方法内部，加上self.后，变量升级为整个对象的成员变量