# -*- encoding: utf-8 -*-

import pymongo

# 连接客户端
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 连接数据库
mydb = myclient["runoobdb"]
# 列表头
mycol = mydb["sites"]

# # 内容
# mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
#
# # 在表头下插入文档
# x = mycol.insert_one(mydict)
# print(x)
# print(x.inserted_id)
#
# mylist = [
#     {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
#     {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
#     {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
#     {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
#     {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
# ]
#
# # 在表头下插入多个文档
# x = mycol.insert_many(mylist)

# # 输出插入的所有文档对应的 _id 值
# print(x.inserted_ids)

# # 查询集合中的所有数据
# print("hold on \n")
# for x in mycol.find():
#     print(x)
#

# # 更新字段，将 alexa 从 10000 更新到 12345
# myquery = {"alexa": "10000"}
# newquery = {"$set": {"alexa": "12345"}}
# mycol.update_one(myquery, newquery)

# # 删除字段，将第一个符合 alexa = ‘100’的字断删除
# myquery = {"alexa": "100"}
# mycol.delete_one(myquery)
# for x in mycol.find():
#     print(x)

# # 对字段 alexa 按降序排序：
# mydoc = mycol.find().sort("alexa", -1)
# for x in mydoc:
#     print(x)
