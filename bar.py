from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

import pymysql

db = pymysql.connect(host='localhost', database='job', user='root', password='wmx13596', port=3306)
cursor = db.cursor()
# 不同岗位中招聘的岗位需求
sql = "select job_title, sum(recruit_number) as 人数 from recruit group by job_title"

cursor.execute(sql)
results = cursor.fetchall()
list1, list2 = [], []
for result in results:
    list1_num = result[0]
    list2_num = result[1]
    list1.append(list1_num)
    list2.append(list2_num)

c = (
    Bar()
    .add_xaxis(list1)
    .add_yaxis("招聘人数", list2)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="不同岗位中招聘的岗位需求"),
        datazoom_opts=opts.DataZoomOpts(),
    )
    .render("bar.html")
)
