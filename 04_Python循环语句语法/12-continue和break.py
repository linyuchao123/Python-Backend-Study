# ========================= continue关键字知识点 =========================
# 作用：中断本次循环，直接跳转到下一次循环，不会终止整个循环
# 适用范围：for循环、while循环都可以使用，两种循环里效果完全一致
from idlelib.colorizer import prog_group_name_to_tag

from IPython.utils.PyColorize import pride_theme

# 逻辑说明：
# 循环运行时，代码执行到continue，立刻结束当前这一轮循环
# continue后续同一缩进层级的代码不会运行，直接开启下一轮循环

# 示例基础结构
# for i in range(1, 100):
#     语句1
#     continue  # 执行到这里，本轮直接终止
#     语句2      # 永远无法执行到

# 详细解释
# 1. 遇到continue，结束当前本次循环，进入下一次循环
# 2. continue下方同层级代码（语句2）不会被执行
# 使用场景：循环过程中满足特定条件时，跳过本轮剩余代码，直接开启下一轮循环

# 演示循环中断语句 continue
for i in range(1,6):
    print("语句1")
    continue
    print("语句2")  # 不会输出语句3，循环依旧会执行

# 演示continue的嵌套应用
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        continue
        print("语句3") # 不会输出语句3，循环依旧会执行

    print("语句4")

# 演示循环中断语句break
for i in range(1,101):
    print("语句1")
    break
    print("语句2")  # 整个循环直接结束

print("语句3")

# 演示break的嵌套应用
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3") # 内层循环遇到break直接结束

    print("语句4")

# 知识点总结：break与continue
# 1. continue的作用：（临时中断）
# 中断所在循环的当次执行，直接进入下一次循环
#
# 2. break的作用： （永久中断）
# 直接结束所在的整个循环
#
# 3. 注意事项：
# ① continue和break，在for和while循环中作用完全一致
# ② 在嵌套循环中，二者仅能作用于自身所在的内层循环，无法影响上层外层循环