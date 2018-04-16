#!/usr/local/bin/python3

from selenium import webdriver

class Driver:

    __driver = None

    def __init__(self):
        if self.__driver is None:
            self.__driver = webdriver.Firefox()
        pass

    # 页面源码
    def page_result(self,url):
        driver = self.__driver
        driver.get(url)
        content = driver.page_source
        driver.close()
        return content

