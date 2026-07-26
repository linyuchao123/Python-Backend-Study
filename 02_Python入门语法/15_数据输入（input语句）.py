"""
    演示python的input语句
    获取键盘的输入信息
"""

print("请告诉我你是谁？")
name = input()
print("我知道了，你是：%s" % name)

input("请告诉我你是谁？")

# 输入数字类型
num = input("请告诉我你的银行卡密码: ")
# 数据类型转换
num = int(num)
print("你的银行卡密码的类型是：",type(num))

# 总结：input语句的功能是：获取键盘输入的数据
#      input(提示信息） 类型永远都是字符串类型