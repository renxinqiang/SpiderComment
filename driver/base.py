#!/usr/local/bin/python3

from driver import Driver
from selenium.common.exceptions import TimeoutException
from log import Log


class Base(Driver):

    # 页面源码
    def page_result(self, url):
        return self.driver.page_source

    # 页面请求
    def get_url(self, url=None):
        if not url:
            return False
        try:
            self.driver.get(url)
        except TimeoutException:
            Log().write_log('Driver','Get Url Faild!!!')
        pass
