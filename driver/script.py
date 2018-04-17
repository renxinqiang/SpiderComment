#!/usr/local/bin/python3

'''
@desc 浏览器交互
@author renxinqiang
'''

from driver import Driver


class Script(Driver):

    def exec_script(self, con):
        if not con:
            return False
        self.driver.execute_script(con)
        pass