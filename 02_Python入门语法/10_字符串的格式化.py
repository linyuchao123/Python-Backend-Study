# 通过展位的形式，完成拼接
name = "黑马程序员"
message = "学IT来: %s"  % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "python大数据学科，北京%s期，毕业平均工资: %s" % (class_num, avg_salary)
print(message)

# %s %表示：我要占位
#    s表示：将变量变成字符串放入占位的地方
"""
    %s：将内容转换成字符串，放入占位位置
    %d：将内容转换成整数，放入占位位置
    %f：将内容转换成浮点型，放入占位位置
"""
name = "传智播客"
setup_year = 2006
stock_price = 19.99
message = "%s, 成立于：%d，我今天的股价是：%f" % (name, setup_year, stock_price)
print(message)
