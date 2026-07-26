# 外层循环控制行数
for i in range(1, 10):
    # 内层循环控制每一行的输出
    for j in range(1,i + 1):
        # 在内层循环中输出每一行的内容
        print(f"{i} x {j} = {i * j}\t",end='')

    # 外层循环可以通过print输出一个回车符
    print()