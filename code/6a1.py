#coding:utf-8
import pandas as pd

import csv

csvfile=file('csvtest.csv','wb')
writer=csv.writer(csvfile)

writer.writerow(['姓名','年龄','电话'])

data=[
	('小河','25','123456'),
	('小芳','23','1254354')
]

writer.writerows(data)

csvfile.close()



