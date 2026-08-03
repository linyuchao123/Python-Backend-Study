# 复写
# 子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以进行复写。
# 即：在子类中重新定义同名的属性或方法即可。

class Phone:
    IMEI = None                 # 序列号
    producer = "ITCAST"         # 厂商

    def call_by_5g(self):
        print("父类的5g通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"        # 复写父类属性

    def call_by_5g(self):       # 复写父类方法
        print("开启CPU单核模式，确保通话的时候省电")
        print("子类的5g通话")
        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)

# 调用父类同名成员
# 一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员
# 如果需要使用被复写的父类的成员，需要特殊的调用方式:

# 方式1：直接通过父类名调用父类成员
# 使用成员变量：父类名.成员变量
# 使用成员方法：父类名.成员方法(self)

# 方式2：使用super()调用父类成员
# 使用成员变量：super().成员变量
# 使用成员方法：super().成员方法()

class Phone:
    IMEI = None                 # 序列号
    producer = "ITCAST"         # 厂商

    def call_by_5g(self):
        print("父类的5g通话")

class MyPhone(Phone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("开启cpu单核模式，确保通话的时候省电")
        # 方式1调用父类成员
        print(f"父类的品牌是：{Phone.producer}")
        Phone.call_by_5g(self)

        # 方式2调用父类成员
        print(f"父类的品牌是：{super().producer}")
        super().call_by_5g()
        print("关闭cpu单核模式，确保性能")
        print("子类的5g通话")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)