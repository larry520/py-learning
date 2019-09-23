
from sqlserver import *

dbObject = MySQL(host='localhost', port=3306, user='root', password='123!@#qqw',db='yiibaidb')
db2 =  MySQL(host='localhost', port=3306, user='root', password='123!@#qqw',db='yiibaidb')
print(dbObject.fetchone(table='superStar',order='id desc'))

res = dbObject.insertMany(table='superStar',
                          value="(16,'张国荣','','霸王别姬',"+str(getTime())+"),(17,'邓紫棋','','差不多女孩',"+str(getTime())+")")
print(res)
print(db2.fetchall(table='superStar'))

