import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from sqlalchemy import create_engine

conn = pymysql.connect(host='localhost', user='root', password='1123',
				db='jh_test', charset='utf8')
curs = conn.cursor()

sql = 'select * from test_table'
curs.execute(sql)

rows = curs.fetchall()
print(type(rows))

df = pd.DataFrame(list(rows), columns=['a','b','c','d'])
print(df.loc[:,['a','b']])

engine = create_engine("mysql+mysqldb://root:1123@localhost:3306/jh_test", echo=False)

#df = pd.DataFrame({'name':['jason','petter'], 'age':[10,15], 'sex':['man','woman']})
#print(df)

df = pd.DataFrame(columns=['name','age','sex'])
name = ['max','potter','rechard']
age = [10, 30, 20]
sex = ['woman', 'man','woman']

col_dic = {'name':name, 'age':age, 'sex':sex}

for i in col_dic.keys():
	df[i] = col_dic.get(i)



df.to_sql(name='test', con=engine, if_exists='append', index=False)

