# pyecharts基础折线图
# 1.导入折线图类Line
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# 2.创建折线图实例
line = Line()

# 3.配置X轴类目数据
line.add_xaxis(["中国", "美国", "英国"])

# 4.配置Y轴系列：系列名称为GDP，对应数值[30,20,10]
line.add_yaxis("GDP",[30, 20, 10])

# 设置全局配置项set_global_opts()来设置
line.set_global_opts(
    title_opts = TitleOpts(title = "GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts = LegendOpts(is_show=True),
    toolbox_opts = ToolboxOpts(is_show=True),
    visualmap_opts = VisualMapOpts(is_show=True),
)
# 5.渲染生成html图表文件，默认render.html
line.render()

# pyecharts配置：全局配置 和 系列配置
