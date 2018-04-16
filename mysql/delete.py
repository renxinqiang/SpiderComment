#!/usr/local/bin/python3

import mysql

class Delete(mysql.MySql):

    def delete(self,sql=''):
        if sql is '':
            return False
        result = self.delete_sql(sql)
        return result