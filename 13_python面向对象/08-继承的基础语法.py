# 单继承语法：class 类名（父类名）：
#               类内容名

# 演示单继承
class Phone:
    IMEI = None   # 序列号
    producer = "ITCAST"  # 厂商

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id = "10001"      # 面部识别ID

    def call_by_5g(self):
        print("2022年新功能：5g通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

# 单继承语法：class 类名（父类1，父类2，父类3......父类N）：
#               类内容名

# 演示多继承
# 父类1：手机
class Phone:
    IMEI = None      # 序列号
    producer = None  # 厂商

    def call_by_5g(self):
        print("5g通话")

# 父类2：NFC读卡器
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("读取NFC卡")

    def write_card(self):
        print("写入NFC卡")

# 父类3：红外遥控器
class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")

# 多继承：MyPhone同时继承Phone、NFCReader、RemoteControl三个父类
class MyPhone(Phone, NFCReader, RemoteControl):
    pass  # 补全语法

phone = MyPhone()
phone.call_by_5g()
phone.write_card()
phone.read_card()
phone.control()

print(phone.producer)

# 1. 什么是继承？
# 继承就是一个类，继承另外一个类的成员变量和成员方法
# 语法:
# class 类(父类[, 父2, ……, 父类N]):
#     类内容体
# 子类构建的类对象，可以
# · 有自己的成员变量和成员方法
# · 使用父类的成员变量和成员方法

# 2. 单继承和多继承
# 单继承: 一个类继承另一个类
# 多继承: 一个类继承多个类，按照顺序从左向右依次继承
# 多继承中，如果父类有同名方法或属性，先继承的优先级高于后继承

# 3. pass关键字的作用是什么
# pass是占位语句，用来保证函数（方法）或类定义的完整性，表示无内容，空的意思