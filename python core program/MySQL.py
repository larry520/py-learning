# -*- encoding: utf-8 -*-

import pymongo
#
# myclient = pymongo.MongoClient("mongodb://localhost:9999/")
# mydb = myclient["runoobdb"]

myclient = pymongo.MongoClient('mongodb://localhost:9999/')

dblist = myclient.list_database_names()
# dblist = myclient.database_names()
if "runoobdb" in dblist:
    print("数据库已存在！")

