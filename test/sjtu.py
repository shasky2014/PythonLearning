nodes = [
    {'name': 'category1'},
    {'name': 'category2'},
    {'name': 'category3'},
    {'name': 'category4'},
    {'name': 'category5'},
    {'name': 'category6'},
]
# nodes需要把桑基图中出现的名称全部设置进去，并且要保证links中的名称与name相同
links = [
    {'source': 'category1', 'target': 'category2', 'value': 10},
    {'source': 'category2', 'target': 'category3', 'value': 15},
    {'source': 'category3', 'target': 'category4', 'value': 20},
    {'source': 'category5', 'target': 'category6', 'value': 25}
]
# links代表节点关系，source表示起点，target表示终点，需要将节点关系全部输入进去，value表示节点长度
from pyecharts import Sankey

sankey = Sankey("名称", width=1600, height=900)  # 可以设置大小和图标名称
# sankey.use_theme('dark') 	#图表主题，pyecharts可以自定义主题，‘dark’可以显示为黑色背景。
sankey.add(
    '按钮',  # 按钮，用来控制是否显示图标。若不显示，可以设置为‘空格’
    nodes,  # 输入节点，如果导入json数据，nodes=json['nodes]
    links,  # 输入关系,nodes=json['links']
    line_opacity=0.6,  # 曲线色彩深度
    line_curve=0.6,  # 曲线弧度
    line_color="target",  # 以target为自动选择颜色的基准，也可以设置为source
    line_width=2,  # 曲线宽度
    is_label_show=True,  # 是否显示标签，默认值为True
    label_text_size=16,  # 设置标签字体大小
    label_pos="right",  # 标签位置，可以设置靠左或靠右
    label_color='颜色',  # 设置标签颜色
    is_random=True,  # 曲线颜色随机排列
    sankey_node_gap=20,  # 桑基图同列上下节点之间的距离，如果做图时字体太密，可以调整一下节点距离。
)
sankey.render()
