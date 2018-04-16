#!/usr/local/bin/python3


import config
import pymysql
import log


class MySql:
    __host = ''
    __user = ''
    __pass = ''
    __db = ''
    __port = ''
    __connect = ''
    __cursor = ''

    def __init__(self):
        self.__host = config.MYSQL['host']
        self.__user = config.MYSQL['user']
        self.__pass = config.MYSQL['password']
        self.__db = config.MYSQL['db']
        self.__port = config.MYSQL['port']
        self.__mysql_connect()
        pass

    # 链接
    def __mysql_connect(self):
        if self.__connect is '':
            try:
                self.__connect = pymysql.connect(self.__host, self.__user, self.__pass, self.__db)
                self.__cursor = self.__connect.cursor()
            except:
                log.Log().write_log(__class__, 'Connect MySql Faild!!!')
        pass

    # 游标
    def __exec(self, sql=''):
        if sql is '':
            return False
        try:
            self.__cursor.execute(sql)
            return self.__cursor
        except:
            log.Log().write_log(__class__, 'Cursor Sql Faild!!!')

    # 查找所有
    def find_all(self, sql=''):
        if sql is '':
            return False
        cursor = self.__exec(sql)
        return cursor.fetchall()

    # 查找一个
    def find_one(self, sql=''):
        if sql is '':
            return False
        cursor = self.__exec(sql)
        return cursor.fetchone()

    # 查找几个
    def find_mony(self, sql='', size=0):
        if sql is '' or size is 0:
            return False
        cursor = self.__exec(sql)
        return cursor.fetchmany(sql, size)

    # 插入
    def insert_sql(self,sql=''):
        if sql is '':
            return False
        self.__exec(sql)
        self.__commit_sql()
        return True

    # 更新
    def update_sql(self,sql=''):
        if sql is '':
            return False
        self.__exec(sql)
        self.__commit_sql()
        return True

    # 删除操作
    def delete_sql(self,sql=''):
        if sql is '':
            return False
        self.__exec(sql)
        self.__commit_sql()
        return True


    # 执行语句
    def __commit_sql(self):
        try:
            self.__connect.commit()
        except:
            self.__connect.rollback()
            log.Log().write_log(__class__,'Commit Sql Faild!!!')

    def __enter__(self):
        return self

    # 关闭
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__connect.close()
