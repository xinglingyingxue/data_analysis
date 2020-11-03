from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.faker import Faker

import pymysql

db = pymysql.connect(host='localhost', database='job', user='root', password='wmx13596', port=3306)
cursor = db.cursor()

# 算法工程师的学历分布图
sql = "select education,count(education) as 人数 from recruit WHERE job_title='算法工程师' group by education"
cursor.execute(sql)
results_info = cursor.fetchall()
results = []
for result in results_info:
    result = list(result)
    results.append(result)

c = (
    Funnel()
    .add(
        "学历",
        # [list(z) for z in zip(Faker.choose(), Faker.values())],
        results,
        sort_="ascending",
        label_opts=opts.LabelOpts(position="inside"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="算法工程师的学历分布图"))
    .render("funnel.html")
)
