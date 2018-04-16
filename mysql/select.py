#!/usr/local/bin/python3

import mysql


class Select(mysql.MySql):

    def result_all(self, sql=''):
        if sql is '':
            return ''
        result = self.find_all(sql)
        return result

    def result_one(self, sql=''):
        if sql is '':
            return ''
        result = self.find_one(sql)
        return result
