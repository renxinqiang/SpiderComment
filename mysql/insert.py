#!/usr/local/bin/pyhton3

import mysql

class Insert(mysql.MySql):

    def insert(self,sql=''):
        if sql is '':
            return False
        result = self.insert_sql(sql)
        return result