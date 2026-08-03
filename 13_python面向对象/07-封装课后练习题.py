# 设计一个类，用来描述手机
class Phone:
    # 提供私有成员变量:__is_5g_enable
    __is__5g_enable = False   # 5g状态

    # 提供私有成员方法：__check__5g
    def __check_5g(self):
        if self.__is__5g_enable:
            print(f"5g开启")
        else:
            print(f"5g关闭，使用4g网络")

# 提供公开成员方法：call_by_5g()
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()
