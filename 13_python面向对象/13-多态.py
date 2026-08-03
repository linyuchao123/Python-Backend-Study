# 多态：多种状态，完成某个行为时，使用不同的对象会得到不同的状态
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)  # 输出：汪汪汪
make_noise(cat)  # 输出：喵喵喵

# 同样的行为（函数），传入不同的对象，得到不同的状态

# 抽象类（接口）
class Animal:
    def speak(self):
        pass  # 空实现方法

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

# 抽象类（接口）
# 抽象类好比定义一个标准，包含抽象方法，要求子类必须实现
class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调核心制冷科技")

    def hot_wind(self):
        print("美的空调电热丝加热")

    def swing_l_r(self):
        print("美的空调无风感左右摆风")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调变频省电制冷")

    def hot_wind(self):
        print("格力空调电热丝加热")

    def swing_l_r(self):
        print("格力空调静音左右摆风")

def make_cool(ac: AC):
    ac.cool_wind()
    ac.hot_wind()


midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)

# 1. 什么是多态？
# 多态指的是，同一个行为，使用不同的对象获得不同的状态。
# 如，定义函数（方法），通过类型注解声明需要父类对象，实际传入子类对象进行工作，从而获得不同的工作状态

# 2. 什么是抽象类（接口）
# 包含抽象方法的类，称之为抽象类。抽象方法是指：没有具体实现的方法（pass）称之为抽象方法

# 3. 抽象类的作用
# 多用于做顶层设计（设计标准），以便子类做具体实现。
# 也是对子类的一种软性约束，要求子类必须复写（实现）父类的一些方法