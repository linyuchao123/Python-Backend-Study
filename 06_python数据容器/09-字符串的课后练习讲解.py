my_str = "itheima itcast boxuegu"
# 统计有多少个"it“字符
num = my_str.count("it")
print(f"字符串{my_str}中有{num}个it字符")

# 将字符串中的空格替换成字符：“｜”
new_my_str = my_str.replace(" ","|")
print(f"字符串{my_str}被空格替换后，结果是：{new_my_str}")

# 并按照“｜”进行字符串分割，得到列表
new_my_list = new_my_str.split("|")
print(f"字符串{new_my_list}按照｜分割后结果是：{new_my_list}")

