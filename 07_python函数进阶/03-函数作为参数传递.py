# 函数可以作为参数传入使用
# 函数作为参数传入 不是数据的传入 而是计算逻辑的传入

# 定义一个函数，接收另一个函数作为传入参数
def test_func(compute):
    result = compute(1,2)  # 确定conpute是函数
    print(f"compute的类型是：{type(compute)}")
    print(f"计算结果:{result}")

# 定义一个函数，准备作为参数传入另一个函数
def compute(x,y):
    return x + y
# 调用，并传入函数
test_func(compute)
