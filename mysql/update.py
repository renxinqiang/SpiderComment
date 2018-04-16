#!/usr/local/bin/python3

import mysql


class Update(mysql.MySql):

    def update(self,sql=''):
        if sql is '':
            return False
        result = self.update_sql(sql)
        return result
