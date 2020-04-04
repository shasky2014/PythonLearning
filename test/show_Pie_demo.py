from IPython.display import SVG, display  # 导入交互式绘图包
import pygal

# pie_chart = pygal.Pie()
#
# # pie_chart.add('title', [10, 20, 30, 5])
# pie_chart.add('p1', [90])
# pie_chart.add('p2', [120])
# pie_chart.add('p3', [779])
# pie_chart.add('other', [1000])
#
# pie_chart.render_in_browser()
from pygal import Pie

# chart = pygal.Pie(inner_radius=.3, pretty_print=True)
# chart.title = 'Browser usage in February 2012 (in %)'
# chart.add('IE', 19.5)
# chart.add('Firefox', 36.6)
# chart.add('Chrome', 36.3)
# chart.add('Safari', 4.5)
# chart.add('Opera', 2.3)
# chart.render_in_browser()

pie = Pie()
pie.add('IE', 19.5)
pie.add('Firefox', 36.6)
pie.add('Chrome', 36.3)
pie.add('Safari', 4.5)
pie.add('Opera', 2.3)

half = Pie(inner_radius=.7,half_pie=True)
half.add('IE', 19.5)
half.add('Firefox', 36.6)
half.add('Chrome', 36.3)
half.add('Safari', 4.5)
half.add('Opera', 2.3)
assert pie.render_in_browser() != half.render_in_browser()
