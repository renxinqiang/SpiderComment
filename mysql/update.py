#!/usr/local/bin/python3

from mysql import MySql


class Update(MySql):

    def update(self,sql=''):
        if not sql:
            return False
        return self.update_sql(sql)