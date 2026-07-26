# 定义键盘输入获取身高数据
height = int(input("请输入你的升高（cm）："))
if height > 120:
    print("您的身高超过120cm，需要买票，10元。")
else:
    print("您的身高低于120cm，可以免费游玩。")
print("祝您游玩愉快。")
