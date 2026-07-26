print("欢迎来到黑马动物园👏")
height = int(input("请输入你的身高(cm)："))
vip_level = int(input("请输入你的VIP等级（1-5）："))
day = int(input("请告诉我今天几号："))

if height < 120:
    print("身高小于120cm，可以免费，。")
elif vip_level > 3:
    print("vip级别大于3，可以免费。")
elif day == 1:
    print("今天是1号免费日，可以免费。")
else:  # else可以省略
    print("不好意思，条件都不满足，需要买票10元。")

print("祝您游玩愉快😀")

# 无定义
if int(input("请输入你的身高(cm):"))<120:
    print("身高小于120cm，可以免费。")
elif int(input("请输入你的VIP等级(1-5):"))>3:
    print("vip级别大于3，可以免费。")
elif int(input("请告诉我今天几号:")) == 1:
    print("今天是1号免费日，可以免费")
else:
    print("不好意思，条件都不满足，需要买票10元。")
