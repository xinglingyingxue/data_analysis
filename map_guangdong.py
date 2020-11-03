from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker


import pymysql

db = pymysql.connect(host='localhost', database='job', user='root', password='wmx13596', port=3306)
cursor = db.cursor()

# 广东省五个沿海城市公司分布图
sql = "select work_place,count(work_place) as 数量 from recruit WHERE work_place='广州市' or work_place='深圳市' or work_place='东莞市' or work_place='佛山市' or work_place='珠海市' group by work_place"
cursor.execute(sql)
results_info = cursor.fetchall()
results = []
for result in results_info:
    result = list(result)
    results.append(result)

c = (
    Map()
    .add("公司", results, "广东")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-广东地图"), visualmap_opts=opts.VisualMapOpts()
    )
    .render("map_guangdong.html")
)
