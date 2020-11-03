from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

import pymysql

db = pymysql.connect(host='localhost', database='job', user='root', password='wmx13596', port=3306)
cursor = db.cursor()
sql = "select * from recruit where job_title like '%数据分析%'"
# sql="select company_nature, count(company_nature) as total from recruit group by company_nature"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
print(len(results))
# for row in results:
#     print(row)
# # 数据分析岗位中各公司的种类
# sql = "select distinct company_nature from recruit where job_title like '%数据分析%'"
# result = cursor.execute(sql)
# results_info = cursor.fetchall()
# results = []
# for result in results_info:
#     print(result)
#     result = list(result)
#     results.append(result)
# print(list(results))
# print(len(results))
# 数据分析岗位中各公司的种类的数量
sql = "select company_nature, count(company_nature) as total from recruit WHERE job_title like '%数据分析%' group by company_nature"
cursor.execute(sql)
results_info = cursor.fetchall()
results = []
for result in results_info:
    print(result)
    result = list(result)
    results.append(result)
print(results)

c = (
    Pie()
    # .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .add("", results)
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="数据分析岗位中各类型企业所占比列"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie.html")
)