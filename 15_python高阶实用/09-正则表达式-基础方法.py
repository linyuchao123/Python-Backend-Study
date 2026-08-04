# 正则表达式
# 正则表达式，又称规则表达式（Regular Expression），是使用单个字符串来描述、匹配某个句法规则的字符串
# 常被用来检索、替换那些符合某个模式（规则）的文本

# 简单来说，正则表达式就是使用：字符串定义规则，并通过规则去验证字符串是否匹配
# 比如，验证一个字符串是否是符合条件的电子邮箱地址，只需要配置好正则规则，即可匹配任意邮箱

# 邮箱格式正则规则：^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$
# 作用：判断一个完整字符串是否为标准邮箱格式

# 对比说明：如果不使用正则，只用 if else 对字符串做格式判断，代码编写难度会非常大

import re
# 邮箱正则表达式
email_pattern = r"^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$"
# ^ 匹配字符串开头；[\w-]+ 匹配用户名合法字符；@ 匹配邮箱分隔符；末尾$匹配字符串结尾
# fullmatch：要求整段内容完全匹配正则，适合格式校验

# 正则的三个基础方法
# Python正则表达式依托re模块实现，核心有match、search、findall三个基础匹配方法

# -------------------- re.match(匹配规则, 被匹配字符串) --------------------
# 匹配逻辑：仅从【字符串开头】尝试匹配
# 匹配成功：返回匹配对象（内含匹配位置、匹配内容等信息）；匹配失败：返回None
import re

# 案例1：字符串开头就是python，可以匹配成功
s = 'python itheima python itheima python itheima'
result = re.match('python', s)
print(result)          # <re.Match object; span=(0, 6), match='python'> 返回匹配对象
print(result.span())   # (0, 6) 获取匹配内容的起止下标
print(result.group())  # python 获取匹配到的具体文本

# 案例2：字符串开头为1，不是python，开头匹配失败
s = '1python itheima python itheima python itheima'
result = re.match('python', s)
print(result)          # None 匹配失败

# 正则的三个基础方法：re.search
# re.search(匹配规则, 被匹配字符串)
# 匹配特点：扫描整个字符串，从前向后查找；找到第一个匹配内容就立刻停止，不再继续向后检索
import re

# 案例1：字符串中间存在python，可匹配成功
s = '1python666itheima666python666'
result = re.search('python', s)
print(result)          # <re.Match object; span=(1, 7), match='python'> 返回匹配对象
print(result.span())   # (1, 7) 获取首个匹配内容的下标区间
print(result.group())  # python 获取匹配到的文本内容

# 案例2：整个字符串内无目标内容，匹配失败返回None
s = 'itheima666'
result = re.search('python', s)
print(result)          # None

# 正则的三个基础方法：re.findall
# re.findall(匹配规则, 被匹配字符串)
# 功能说明：遍历整个字符串，找出所有符合规则的匹配项，以列表形式返回
import re

# 案例1：字符串中有两处python，全部提取
s = '1python666itheima666python666'
result = re.findall('python', s)
print(result)  # ['python', 'python']

# 案例2：字符串中不存在itcast，匹配不到则返回空列表
s = '1python666itheima666python666'
result = re.findall('itcast', s)
print(result)  # []

# 一、正则表达式定义
# 本质：字符串校验规则
# 实现形式：特殊字符拼接成规则模板
# 用途：判断待测字符串是否匹配模板，例如下方邮箱正则
# 邮箱正则：^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$

# 二、re模块三大方法区分
# 1. re.match
#    匹配范围：仅限字符串起始位置
#    返回特点：仅返回第一个匹配结果
# 2. re.search
#    匹配范围：遍历整个字符串（全局）
#    返回特点：找到第一个匹配结果就停止
# 3. re.findall
#    匹配范围：遍历整个字符串（全局）
#    返回特点：收集全部匹配结果，以列表返回