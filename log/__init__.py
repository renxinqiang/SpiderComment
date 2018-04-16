#!/usr/local/bin/python3

import config


class Log:
    __dir = ''

    def __init__(self):
        self.__dir = config.LOG
        pass

    def write_log(self, msg='', dir=''):
        if msg is '' or dir is '':
            return False
        file = open(self.__dir[dir], 'wb+')
        file.write(msg)
        file.close()
