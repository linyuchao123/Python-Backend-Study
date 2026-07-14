# 方式1： 使用print直接输出类型信息
print(type("黑马程序眼"))
print(type(666))
print(type(13.14))

# 方式2： 使用变量存储type()语句的结果
string_type = type("黑马程序员")
int_type = type(666)
float_type = type(11.345)
print(string_type)
print(int_type)
print(float_type)

# 方式3： 使用typ()语句，查看变量中存储的数据类型信息
name = "黑马程序员"
name_type = type(name)
print(name_type)

# 变量没有类型  但是变量存储的数据是有类型的