#!/usr/local/bin/python3

from mysql import MySql


class Select(MySql):

    def result_all(self, sql=''):
        if not sql:
            return ''
        return self.find_all(sql)

    def result_one(self, sql=''):
        if not sql:
            return ''
        return self.find_one(sql)
