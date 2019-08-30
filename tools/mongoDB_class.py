# -*- encoding：UTF-8 -*-
#  can use Robo 3T for visualization
"""
class Database is used for MongoDB option


"""

from pymongo import MongoClient


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

    # 查询数据返回列表头
    def find(self, col, condition, column=None):
        if self.get_state():
            if column is None:
                return self.db[col].find(condition)
            else:
                return self.db[col].find(condition, column)
        else:
            return None

    # 查询数据返回符合要求数量
    def find_counts(self, col, condition, column=None):
        if self.get_state():
            if column is None:
                return self.db[col].count_documents(condition)
            else:
                return self.db[col].count_documents(condition, column)
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
    print(time.strftime('%Y-%m-%d %X'))
    start_time = int(time.time() * 1e6)

    for i in range(10):
        t = int(time.time() * 1e6)
        db.insert_one("ut", {"username": int(i),
                             "timestamp": t,
                             "password": "123",
                             "telephone": int(random.random() * 1000000)})

    # $lt:<   $gt：> $lte: <= $gte:>=  $ne: !=  $in 在范围内  $nin 不在范围内  $regex 匹配正则表达式
    print("deleted count: ", db.delete("ut", {"username": {"$gte": 3}}))
    print('2.', db.update("ut", {"username": [3, 0]}))
    results = db.find("ut", {})  # results使用后自动重置为空列表
    for i, result in enumerate(results):
        print(i, result)
    print(list(results))  # results使用后自动重置为空列表
    time.sleep(0.001)
    print('3.', db.find_counts("ut",  {"password": "123", "username": 0}))
