# 什么是json
# 1. JSON是一种轻量级的数据交互格式，可以按照JSON指定格式组织、封装数据
# 2. JSON本质是拥有固定格式的字符串

# 主要功能：
# JSON是多编程语言通用的数据格式，用于不同编程语言之间的数据传输、交互
# 类比：
# 英语：全世界通用语言
# 普通话：国内多民族通用交流语言

# json有什么用
# 不同编程语言的数据存储容器不一样：Python有字典dict，很多其他编程语言没有完全对应的类型
# JSON充当跨语言中转格式，解决不同语言之间数据无法直接互通传输的问题

# 数据传输流程举例（Python ↔ C语言）
# 1. Python发数据：Python原生数据 → 转为JSON字符串 → C语言接收JSON → 转成C语言可识别的数据使用
# 2. C语言发数据：C原生数据 → 转为JSON字符串 → Python接收JSON → 转成字典/列表等Python数据使用
# JSON作为统一中间载体，实现所有编程语言互相传递数据

# json格式数据转化
# JSON格式规范严格，仅支持两种最外层结构：大括号对象、中括号数组

# 格式1：外层大括号{}（键值对结构）
# {"name":"admin","age":18}

# 格式2：外层中括号[]（数组，内部存放多个JSON对象）
# [{"name":"admin","age":18},{"name":"root","age":16},{"name":"张三","age":20}]

# 重要硬性规则：JSON里所有键名必须使用双引号""，不能用单引号''

# Python数据和Json数据的相互转化
# 操作必须导入python内置json模块
import json

# 1. 准备Python列表/字典数据（可转为JSON）
data = [{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]

# 2. python → json字符串：json.dumps()
json_str = json.dumps(data,ensure_ascii=False)  # ensure_ascii=False 表示中文正常显示
print(f"type(json_str)")
print(json_str)

# 3. json字符串 → python列表/字典：json.loads()
d = {"name":"周杰伦","addr":"台北"}
json_str = json.dumps(d,ensure_ascii=False)
print(f"type(json_str)")
print(json_str)

# 将JSON字符串转换成python数据类型[k:v,k:v],{k:v,k:v}
s = '[{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]'
l = json.loads(s)
print(type(l))
print(l)

# 将JSON包字符串转换成python数据类型[{k:v,k:v}
s = '{"name":"周杰伦","addr":"台北"}'
d = json.loads(s)
print(type(d))
print(d)

# 总结
# dumps：Python对象转JSON字符串
# loads：JSON字符串转回Python原生数据