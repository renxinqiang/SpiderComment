#!/usr/local/bin/python3


import config
import log

import pymysql


class MySql:
    __host = ''
    __user = ''
    __pass = ''
    __db = ''
    __port = ''
    __charset = ''
    __connect = ''
    __cursor = ''

    def __init__(self):
        self.__host = config.MYSQL['host']
        self.__user = config.MYSQL['user']
        self.__pass = config.MYSQL['password']
        self.__db = config.MYSQL['db']
        self.__port = config.MYSQL['port']
        self.__charset = config.MYSQL['charset']
        self.__mysql_connect()
        pass

    # 链接
    def __mysql_connect(self):
        if not self.__connect:
            try:
                self.__connect = pymysql.connect(self.__host, self.__user, self.__pass, self.__db, charset = self.__charset)
                self.__cursor = self.__connect.cursor()
            except:
                log.Log().write_log(__class__, 'Connect MySql Faild!!!')
        pass

    # 游标
    def __exec(self, sql=''):
        if not sql:
            return False
        try:
            self.__cursor.execute(sql)
            return self.__cursor
        except:
            log.Log().write_log(__class__, 'Cursor Sql Faild!!!')

    # 查找所有
    def find_all(self, sql=''):
        if not sql:
            return False
        cursor = self.__exec(sql)
        return cursor.fetchall()

    # 查找一个
    def find_one(self, sql=''):
        if not sql:
            return False
        cursor = self.__exec(sql)
        return cursor.fetchone()

    # 查找几个
    def find_mony(self, sql='', size=0):
        if not sql or size is 0:
            return False
        cursor = self.__exec(sql)
        return cursor.fetchmany(sql, size)

    # 插入
    def insert_sql(self,sql=''):
        if not sql:
            return False
        self.__exec(sql)
        self.__commit_sql()
        return True

    # 更新
    def update_sql(self,sql=''):
        if not sql:
            return False
        self.__exec(sql)
        self.__commit_sql()
        return True

    # 删除操作
    def delete_sql(self,sql=''):
        if not sql:
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
    def close_connect(self):
        self.__cursor.close()
        self.__connect.close()
