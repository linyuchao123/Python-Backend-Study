# for循环语句，本质上是遍历：序列类型
# range语法

# ========== range 语法1：range(num) ==========
# 作用：获取一个从0开始，到num结束的数字序列（不包含num本身）
# 示例：range(5) 生成序列 [0, 1, 2, 3, 4]

# ========== range 语法2：range(num1, num2) ==========
# 作用：获得一个从num1开始，到num2结束的数字序列（不包含num2本身）
# 示例：range(5, 10) 生成序列 [5, 6, 7, 8, 9]

# ========== range 语法3：range(num1, num2, step) ==========
# 作用：获得一个从num1开始，到num2结束的数字序列（不包含num2本身）
# step：数字之间的步长，step默认值为1
# 示例：range(5, 10, 2) 生成序列 [5, 7, 9]

# range语法1 range(num)
range(10)
for x in range(10):
    print(x)

# range语法2 range(num1,num2)
for i in range(5,10):
    print(i)

# range语法3 range(num1,num2,step)
for a in range(5,10,2):
    # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间的间隔为2
    print(a)

for y in  range(10):
    print("送玫瑰花")

"""
range函数知识点总结
1. 功能：生成一段连续/有固定间隔的数字序列
2. 三种语法：
    语法1：range(num)
    语法2：range(num1, num2)
    语法3：range(num1, num2, step)
3. 规则说明：
    语法1：起点0，终点num，不含num
    语法2：起点num1，终点num2，不含num2
    语法3：起点num1，终点num2，不含num2，步长为step
"""