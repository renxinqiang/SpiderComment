#!/usr/local/bin/python3

from mysql import MySql


class Delete(MySql):

    def delete(self, sql=''):
        if not sql:
            return False
        return self.delete_sql(sql)
