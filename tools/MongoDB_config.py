# -*- encoding:UTF-8 -*-

"""
用于初次配置MongoDB 环境

"""

import os


class MongoDBConfig(object):

    def __init__(self):
        # 配置数据库数据路径
        self.dp_path = r' -dbpath "D:\MongDBdata\data"'
        # 配置log路径
        self.log_path = r' -logpath "D:\MongDBdata\log\mongod.log"'
        # 配置文件，并将mongodb作为系统服务启动
        self.file_path = r'C:\Program Files\MongoDB\Server\4.0\mongod.conf'

    # 配置数据库路径
    def data_config(self):
        config = r'mongod ' + self.dp_path + self.log_path + r' -install -serviceName "MongoDB"'
        print(config)
        result = os.system(config)

    # 配置数据库服务
    def services(self):
        service = r'mongod --config ' + self.file_path + ' --install -serviceName "MongoDB"'
        print(service)
        result = os.system(service)

    # 启动服务
    def start_sercives(self,):
        result = os.system(r'net start MongoDB')
        print(result)

    # 关闭服务
    def stop_sercives(self):
        os.system(r'net stop MongoDB')

    # 账号配置
    def account(self):
        os.system(r'use admin')
        os.system(r'db.createUser(')
        os.system(r'{')
        os.system(r'user:"root",')
        os.system(r'pwd:"123456",')
        os.system(r'roles:[{')
        os.system(r'role:"root",')
        os.system(r'db:"admin"')
        os.system(r'}')
        os.system(r']')
        os.system(r'}')
        os.system(r');')


if __name__ == "__main__":

    mongo = MongoDBConfig()
    # mongo.data_config()
    # mongo.start_sercives()
    # mongo.stop_sercives()
    # mongo.account()




