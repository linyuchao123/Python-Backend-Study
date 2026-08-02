# 什么是第三方包
# 包可以包含多个Python模块，每个模块拥有各类功能，包是同类功能的集合体

# 第三方包：非Python官方提供的包，能够大幅提升开发效率
# 常用第三方包举例：
# 科学计算：numpy
# 数据分析：pandas
# 大数据计算：pyspark、apache-flink
# 图形可视化：matplotlib、pyecharts
# 人工智能：tensorflow

# 补充说明：
# 第三方包不属于Python内置内容，无法直接导入，必须手动安装后才能导入使用

# 快速通过网络安装第三方包：pip install 包名称
# pip的网络优化
# pip默认连接国外服务器下载第三方包，下载速度经常很慢

# 使用国内清华镜像源加速安装命令格式：
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称

# 地址说明
# https://pypi.tuna.tsinghua.edu.cn/simple 是清华大学开源镜像站，用来加速pip下载第三方Python包

# 在pycharm中安装包：打开解释器设置选择包进行安装