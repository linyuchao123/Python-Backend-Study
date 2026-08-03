# 工厂模式
# 当需要大量创建一个类的实例的时候，可以使用工厂模式。
# 即，从原生的使用类的构造去创建对象的形式
# 迁移到，基于工厂提供的方法去创建对象的形式。

# class Person:
#     pass
#
# class Worker(Person):
#     pass
#
# class Student(Person):
#     pass
#
# class Teacher(Person):
#     pass
#
# worker = Worker()
# stu = Student()
# teacher = Teacher()