# 处理数据
import json

f_us = open("python.txt","r",encoding="utf-8")
us_data = f_us.read()
# 去掉不和json规范的开头
us_data = us_data.replace(" "," ")
# 去掉不和json的结尾
us_data = us_data[:-2]
# json转python字典
us_dict = json.loads(us_data)

# 获取trend key
trend_data = us_dict["data"][0]["trend"]

x_data = trend_data['updateDate']

y_data = trend_data['list'][0]['data'][:314]
