# 练习案例：序列切片实践
# 原字符串："万过薪月，员序程马黑来，nohtyP学"
# 目标：拼接出 黑马程序员
# 思路1：切片截取【员序程马黑】，使用步长-1反转字符串
# 思路2：split按中文逗号拆分，取出中间内容；replace删除"来"；最后整体倒序
# 核心知识点：字符串切片、split分割、replace替换、负数步长倒序

my_str = "万过薪月，员序程马黑来，nohtyP学"
# 倒序字符串，切片取出
result1 = my_str[::-1][9:14]
print(f"方式1结果：{result1}")

# 切片取出，然后倒序
result2 = my_str[5:10][::-1]
print(f"方式2结果：{result2}")

# split分割“，“ replace替换“来”为空，倒序字符串
result3 = my_str.split("，")[1].replace("来", "")[::-1]
print(f"方式3结果：{result3}")