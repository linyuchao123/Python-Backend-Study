# 综合案例：黑马ATM
# 1. 定义一个全局变量：money，用来记录银行卡余额（默认5000000）
# 2. 定义一个全局变量：name，用来记录客户姓名（启动程序时输入）

# 3. 需要定义如下4个函数：
#    · 查询余额函数
#    · 存款函数
#    · 取款函数
#    · 主菜单函数

# 4. 功能要求：
# ① 程序启动后要求输入客户姓名
# ② 查询余额、存款、取款后都会返回主菜单
# ③ 存款、取款后，都应显示一下当前余额
# ④ 客户选择退出即可结束程序，输入其他数字提示错误

# 定义全局变量money name
money = 5000000
name = None
# 要求客户输入姓名
name = input("请输入您的姓名：")
# 定义查询函数
def query(show_header):
    if show_header:
        print("-----------------查询余额----------------")
    print(f"{name},您好，您的余额剩余:{money}元")

# 定义存款函数
def saving(num):
    global money  # money在函数内部定义为全局变量
    money += num
    print("------------------存款------------------")
    print(f"{name},您好，您存款{num}元成功。")

    # 调用query函数查询余额
    query(False)

# 定义取款函数
def get_money(num):
    global money
    money -= num
    print("-------------------取款-----------------")
    print(f"{name},您好，您取款{num}元成功。")

    # 调用query函数查询余额
    query(False)

# 定义主菜单函数
def main():
    print("-----------------主菜单----------------")
    print(f"{name},您好，欢迎来到黑马银行ATM机，请选择操作")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】") # 通过\t制表符来对齐输出
    print("退出\t\t【输入4】")
    return input("请输入你的选择：")

# 设置无限循环，确保程序不退出
while True:
     keyboard_input = main()
     if keyboard_input == "1":
         query(True)
         continue # 通过continue继续下一次循环，一进来就是回到了主菜单
     elif keyboard_input == "2":
        num = int(input("您想要存入多少钱，请输入："))
        saving(num)
        continue
     elif keyboard_input == "3":
         num = int(input("您想要取多少钱？请输入："))
         get_money(num)
         continue
     else:
         print("程序退出啦")
         break # 通过break退出循环


