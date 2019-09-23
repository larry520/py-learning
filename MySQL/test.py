
from MySQL.sqlserver import *

dbObject = MySQL_sgmode(host='localhost', port=3306, user='root', password='123!@#qqw',db='cygdmdb')
db2 =  MySQL_sgmode(host='localhost', port=3306, user='root', password='123!@#qqw',db='cygdmdb')
print(dbObject.fetchone(table='superStar',order='id desc'))

res = dbObject.insertMany(table='superStar',
                          value="(16,'张国荣','','霸王别姬',"+str(getTime())+"),(17,'邓紫棋','','差不多女孩',"+str(getTime())+")")
print('result: ',res)
print(db2.fetchall(table='superStar'))

