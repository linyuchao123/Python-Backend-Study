"""
    演示python中
    if else的组合判断语句
"""
print("欢迎来到黑马儿童游乐园，儿童免费，成人10元。")
age = int(input("请输入你的年龄:"))
if age >= 18:
    print("您已成年，需要买票10元。")
else:
    print("您未成年，可以免费游玩。")

print("祝您游玩愉快。")

# 总结：else不需要判断条件 if不满足 执行else 需要四个代码块进行缩进。