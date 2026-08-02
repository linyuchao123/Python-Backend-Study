# 类和对象：基于类创建对象的语法:对象名 = 类名称()
# 设计一个闹钟类
class Clock:
    id = None  # 序列话
    price = None

    def ring(self):
        # 跨平台通用模拟响铃
        print("滴滴滴！闹钟响了")

# 构建2个闹钟对象并让其工作
clock1 = Clock()
clock1.id = "003002"
clock1.price = 19.99
print(f"闹钟ID：{clock1.id},价格：{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "003003"
clock2.price = 9.99
print(f"闹钟ID：{clock2.id},价格：{clock2.price}")
clock2.ring()

# 1. 现实世界事物的两大组成：
# - 属性（特征信息）
# - 行为（能做的动作）
# 类同样可以包含属性与行为，因此很适合用类来描述现实里的各类事物

# 2. 类和对象的关系
# 类 = 程序里的设计图纸（通用模板）
# 对象 = 根据图纸制作出来的真实具体实体

# 3. 面向对象编程的含义
# 面向对象编程，就是依托类创建对象，依靠对象完成各项业务工作