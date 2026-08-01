# return接收多个函数返回值
def test_return():
    return 1, 2, 3   # 类型并不限制

x,y,z = test_return()
print(x)
print(y)
print(z)

