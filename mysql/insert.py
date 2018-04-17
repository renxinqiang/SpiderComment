#!/usr/local/bin/pyhton3

from mysql import MySql


class Insert(MySql):

    def insert(self, sql=''):
        if not sql:
            return False
        return self.insert_sql(sql)
