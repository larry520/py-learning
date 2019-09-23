# -*- encoding: utf-8 -*-
# author: larry
# date : 2019.09.18

"""
MySQL 基本操作

USE databaseName // 在操作之前需要用来指定选择要使用的数据库

查
    SELECT column1,column2...    // SELECT * 表示选中所有条目
    FROM tables1,tables2...
    WHERE conditions;

增
    INSERT INTO table(column1,column2...)   // INSERT INTO table 为所有列增加相应值
    VALUES (value1-1,value1-2...)
           (value2-1,value2-2...);  //每个括号对里面表示一行数据

    // 从table2中复制column1,column2列数据到table1中
    INSERT INTO table1
    SELECT column1,column2 FROM table2;

删
    DELETE FROM tableName
    WHERE condition;    // 删除符合条件的行，如果不加约束则删除整个表格

    DELETE FROM tableName
    ORDER BY c1
    LIMIT rowCount;    // 按c1排序，删除前rowCount个数据

改
    UPDATE LOW_PRIORITY table1    // LOW_PRIORITY 修饰符表示延迟更新，无数据读取时更新
    SET
        column1 = value1
        column2 = value2
    WHERE
        conditions;

创建数据库
    CREATE DATABASE IF NOT EXISTS databaseName;

    SHOW DATABASES // 显示所有数据库
删除数据库
    DROP DATABASE IF EXISTS databaseName；   // IF EXISTS 可选修饰符
创建表格
    CREATE TABLE tableName LIKE table1; //创建一个格式和table1一样的空表格

    CREAT TABLE IF NOT EXISTS tableName(
        columnName dataType(size) [NOT NULL|NULL] [DEFAULT VALUE] [AUTO_INCREMENT]
    )

    example:
    CREATE TABLE IF NOT EXISTS tasks (
      task_id INT(11) NOT NULL AUTO_INCREMENT,
      subject VARCHAR(45) DEFAULT NULL,
      start_date DATE DEFAULT NULL,
      end_date DATE DEFAULT NULL,
      description VARCHAR(200) DEFAULT NULL,
      PRIMARY KEY (task_id)
    ) ENGINE=InnoDB;

修改表
    // 添加列，删除列，更改列的数据类型，添加主键，重命名表等
    ALTER TABLE tableName action1[,action2,...]

    // 添加两个或多个列
    ALTER TABLE table
    ADD [COLUMN] column_name_1 column_1_definition [FIRST|AFTER existing_column],
    ADD [COLUMN] column_name_2 column_2_definition [FIRST|AFTER existing_column],
    ...;



部分语法

Now()  当前时间



"""

import pymysql
import hashlib
import time


class MySQL_sgmode(object):
    """
    MySQL 单例模式 增删查改
    """
    # 数据库对象
    __db = None
    # 游标对象
    __cursor = None

    def __new__(self, *args, **kwargs):
        """
        单例模式
        :param args:
        :param kwargs:
        :return:
        """
        if not hasattr(self, '_instance'):
            self._instance = super().__new__(self)
            # 主机
            host = 'host' in kwargs and kwargs['host'] or 'localhost'
            port = 'port' in kwargs and kwargs['port'] or '3306'
            # 用户名
            user = 'user' in kwargs and kwargs['user'] or 'root'
            # 密码
            password = 'password' in kwargs and kwargs['password'] or '123!@#qqw'
            # 数据库
            db = 'db' in kwargs and kwargs['db'] or ''
            # 编码
            charset = 'charset' in kwargs and kwargs['charset'] or 'utf8'
            # 打开数据库连接
            print('连接数据库', db)
            self.__db = pymysql.connect(host=host, port=int(port), user=user, password=password,
                                        db=db, charset=charset)
            # 创建一个游标对象
            # self.__cursor = self.__db.cursor()
            # 返回结果包含字段
            self.__cursor = self.__db.cursor(cursor=pymysql.cursors.DictCursor)
        return self._instance

    # 返回执行execute()方法后影响的行数
    def execute(self, _sql):
        """
        返回受影响的行数
        :param _sql:
        :return:
        """
        self.__cursor.execute(_sql)
        rowcount = self.__cursor.rowcount
        return rowcount

    def insertOne(self, **kwargs):
        """
        增加单条数据，返回自增id。 table, column
        :param kwargs: table, column
        :return:  新增id
        """

        table = kwargs['table']
        del kwargs['table']

        sql = 'insert into %s set ' % table
        for k, v in kwargs.items():
            sql += "%s='%s'," % (k, v)
        sql = sql.rstrip(',')  # 删除最后面的 ','
        print(sql)
        res = None
        try:
            # 执行sql语句
            self.__cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
            # 获取自增id
            res = self.__cursor.lastrowid
        except Exception as e:
            # 发生错误时回滚
            self.__db.rollback()
            # 打印错误
            print(e)
        return res

    def insertMany(self, **kwargs):
        """
        增加多条数据，返回自增id。 table, column
        :param kwargs: table, column
        :return:  新增id
        """
        table = kwargs['table']
        key = 'key' in kwargs and str(kwargs['key']) or ''
        value = kwargs['value']
        sql = 'insert into %s %s values %s ' % (table,key,value)
        print(sql)
        res = None
        try:
            # 执行sql语句
            self.__cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
            # 获取自增id
            res = self.__cursor.lastrowid
        except Exception as e:
            # 发生错误时回滚
            self.__db.rollback()
            # 打印错误
            print(e)
        return res


    def delete(self, **kwargs):
        """
        删除 返回受影响的行数
        :param kwargs: table, where
        :return: int 受影响的行数
        """
        table = kwargs['table']
        where = 'where' in kwargs and 'where '+ kwargs['where'] or ''
        sql = 'delete from %s %s' % (table, where)
        print(sql)
        rowcount = None
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
            # 影响的行数
            rowcount = self.__cursor.rowcount
        except Exception as e:
            # 发生错误时回滚
            self.__db.rollback()
            print(e)
        return rowcount

    def update(self, **kwargs):
        """
        更改，返回影响的行数
        :param kwargs: table, where
        :return: int 影响的行数
        """

        table = kwargs['table']
        kwargs.pop('table')

        where = kwargs['where']
        kwargs.pop('where')

        sql = 'update %s set ' % table
        for k, v in kwargs.items():
            sql += "%s='%s'," % (k, v)
        sql = sql.rstrip(',')
        sql += ' where %s' % where
        print(sql)
        rowcount = None
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
            # 影响的行数
            rowcount = self.__cursor.rowcount
        except Exception as e:
            # 发生错误时回滚
            self.__db.rollback()
            print(e)
        return rowcount

    def fetchone(self, **kwargs):
        """
        查 -> 单条数据 返回查询数据 table,field,where,order
        :param kwargs: table,field,where,order
        :return: 查询结果
        """
        table = kwargs['table']
        # 字段
        field = 'field' in kwargs and kwargs['field'] or '*'
        # where
        where = 'where' in kwargs and 'where ' + kwargs['where'] or ''
        # order
        order = 'order' in kwargs and 'order by ' + kwargs['order'] or ''

        sql = 'select %s from %s %s %s limit 1' % (field, table, where, order)
        print(sql)
        data = None
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 使用 fectchone()方法获取单条数据。
            data = self.__cursor.fetchone()
        except Exception as e:
            # 发生错误时回滚
            self.__db.rollback()
            print(e)
        return data

    def fetchall(self, **kwargs):
        """
        查询多条数据
        :param kwargs:
        :return: 查询结果
        """
        table = kwargs['table']
        # 字段
        field = 'field' in kwargs and kwargs['field'] or '*'
        # where
        where = 'where' in kwargs and 'where ' + kwargs['where'] or ''
        # order
        order = 'order' in kwargs and 'order by ' + kwargs['order'] or ''
        # limit
        limit = 'limit' in kwargs and 'limit ' + kwargs['limit'] or ''
        sql = 'select %s from %s %s %s %s' % (field, table, where, order, limit)
        print(sql)
        data = None
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 使用fetchall()获取所有数据
            data = self.__cursor.fetchall()
        except Exception as e:
            self.__db.rollback()
            print(e)
        return data

    # 析构函数，释放对象时使用
    def __del__(self):
        # 关闭数据库连接
        self.__db.close()
        print('关闭数据库连接')


# 获取时间戳
def getTime():
    return round(time.time())

# 生成md5
def makeMd5(mstr):
    hmd5 = hashlib.md5()
    hmd5.update(mstr.encode('utf-8'))
    return hmd5.hexdigest()

# 时间格式化
def timeFormat(timestamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))



if __name__ == "__main__":
    dbObject = MySQL_sgmode(host='localhost', port=3306, user='root', password='123!@#qqw',db='yiibaidb')

    print('创建数据库：cygdmdb')
    sql = "CREATE DATABASE IF NOT EXISTS cygdmdb"
    res = dbObject.execute(sql)
    print(res)

    print('使用数据库 cygdmdb:')
    sql = "USE cygdmdb"
    res = dbObject.execute(sql)
    print(res)

    print('删除表')
    sql = "DROP TABLE IF EXISTS superStar;"
    dbObject.execute(sql)

     # 创建表
    time.sleep(1)
    print('创建表：')
    sql = """
    CREATE TABLE IF NOT EXISTS superStar(
      id INT(11) NOT NULL AUTO_INCREMENT,
      name VARCHAR(45) DEFAULT NULL,
      age VARCHAR(20) DEFAULT NULL,
      description VARCHAR(200) DEFAULT NULL,
      insert_time INT(11) NOT NULL,
      PRIMARY KEY (id)
    ) ENGINE=InnoDB;
    """
    print(sql)
    res = dbObject.execute(sql)
    print(res)

    # 插入数据
    print('\n插入单条数据: ')
    description = makeMd5('To be No.1')
    insert_time = getTime()
    res = dbObject.insertOne(table='superStar',name='larry',
                          insert_time=insert_time,description=description)
    print(res)

    time.sleep(1)
    insert_time = getTime()
    res = dbObject.insertOne(table='superStar', name='刘亦菲',
                          insert_time=insert_time,
                          description="我只想做个安静的小龙女 ")
    print(res)

    time.sleep(1)
    insert_time = getTime()
    res = dbObject.insertOne(table='superStar', name='刘若英',
                            insert_time=insert_time,
                            description="你听过《亲爱的路人》吗")
    print(res)

    time.sleep(1)
    res = dbObject.insertMany(table='superStar', key="(name,insert_time,description)",
                              value="('张国荣'," + str(getTime()) + ",'霸王别姬'),"
                                    "('邓紫棋'," + str(getTime()) + ",'差不多女孩')")
    print(res)


    # 查询数据-单条
    print('\n查询数据-单条：')
    res = dbObject.fetchall(table='superStar')
    print(res)

    # 修改数据
    print('\n修改数据：')
    res = dbObject.update(table='superStar', where="id=1", description='俺老孙来也！')
    print(res)

    # 删除数据
    print('\n删除数据：')
    res = dbObject.delete(table='superStar', where="id=1")
    print(res)

    #查询数据-多条
    print('\n查询数据-多条：')
    res = dbObject.fetchall(table='superStar',order='id desc')
    print(res,type(res))
    if res:
        res = sorted(res,key=lambda key:key['insert_time'])
        for value in res:
            print('name:%s, date:%s'%(value['name'],timeFormat(value['insert_time'])))

