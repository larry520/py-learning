# -*- encoding：UTF-8 -*-
# reference web：https://blog.csdn.net/wang7807564/article/details/83213389
# robo 3T

from pymongo import MongoClient
from pymongo import collection


class Database(object):
    def __init__(self, address, port, database):
        self.conn = MongoClient(host=address, port=port)
        self.db = self.conn[database]

    # 查询数据库是否连接
    def get_state(self):
        return self.conn is not None and self.db is not None

    # 插入一条数据并返回数据对应id
    def insert_one(self, col, data):
        if self.get_state():
            ret = self.db[col].insert_one(data)
            # print("insert_0k!")
            return ret.inserted_id
        else:
            return ''

    # 插入多条数据并返回数据对应id 列表
    def insert_many(self, col, data):
        if self.get_state():
            ret = self.db[col].insert_many(data)
            return ret.inserted_ids

    # 更新数据，成功返回。。失败返回 0
    def update(self, col, data):
        # data format:
        # {key:[old_data, new_data]}
        data_filter = {}
        data_revised = {}
        for key in data.keys():
            data_filter[key] = data[key][0]
            data_revised[key] = data[key][1]
        if self.get_state():
            return self.db[col].update_many(
                data_filter, {"$set": data_revised}).modified_count
        return 0

    # 查询数据
    def find(self, col, condition, column=None):
        if self.get_state():
            if column is None:
                return self.db[col].find(condition)
            else:
                return self.db[col].find(condition, column)
        else:
            return None

    # 删除数据并返回删除数据条数
    def delete(self, col, condition):
        if self.get_state():
            return self.db[col].delete_many(filter=condition).deleted_count
        return 0


if __name__ == "__main__":
    # unit test
    import time
    import random

    db = Database("localhost", 27017, "hello_MongoDB")
    print(db.get_state())
    print(db.delete("db", {}))
    print(time.time())
    start_time = int(time.time() * 1e6)
    for i in range(10):
        t = int(time.time() * 1e6)
        db.insert_one("ut", {"username": int(i),
                             "timestamp": t,
                             "password": "123",
                             "telephone": int(random.random() * 1000000)})
    # $lt:<   $gt：> $lte: <= $gte:>=  $ne: !=  $in 在范围内  $nin 不在范围内  $regex 匹配正则表达式
    print("deleted count: ", db.delete("ut", {"username": {"$gt": 2}}))
    results = db.find("ut", {})
    for i, result in enumerate(results):
        print(i, result)
    print('2.', db.update("ut", {"password": ["123", "bbb"]}))
    print('3.', db.find("ut",  {"password": "123", "username": 1}))
