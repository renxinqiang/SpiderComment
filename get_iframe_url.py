#!/usr/local/bin/python3

from request import content
from selenium import webdriver
import soup.dom as dom
import soup.attribute as attr
from mysql import insert
from mysql import select


class Get_iframe_url():

    __comment_url = ''

    __doc_url = ''

    __page_source = ''

    __put_data = []

    __comment_host = 'http://comment.zol.com.cn'

    __iframe_id = ''

    def __init__(self,url,type):
        self.__iframe_id = type
        self.__doc_url = url
        self.get_page_source()
        self.set_data()
        self.save_data()
        pass

    def get_page_source(self):
        driverOptions = webdriver.FirefoxOptions()
        driverOptions.set_headless()
        driver = webdriver.Firefox(firefox_options=driverOptions)
        driver.get(self.__doc_url)
        driver.switch_to.frame(self.__iframe_id)
        self.__comment_url = driver.find_element_by_css_selector('.more-comments a').get_attribute('href')
        driver.close()
        self.__page_source = content.Content().text(self.__comment_url, None)
        pass

    def set_data(self):
        select = dom.Dom(self.__page_source).find_select('.page a')
        for i in select:
            href = attr.Attribute().get_attr(i,'href')
            if not href:
                continue
            if self.__put_data.count(self.__comment_host + href) == 1:
                continue
            # 将链接扔到列表中
            self.__put_data.append(self.__comment_host + href)
        # 将首页链接扔到列表中
        self.__put_data.append(self.__comment_url)
        pass

    def save_data(self):
        data = self.__put_data
        for x in data:
            select_sql = "select * from iframe_url where iframe_url = '" + x + "'"
            res = select.Select().find_one(select_sql)
            if res:
                continue

            sql = "INSERT INTO iframe_url (iframe_url)" \
                  "VALUES ('" + str(x) + "')"
            insert.Insert().insert(sql)
        pass


if __name__ == '__main__':
    Get_iframe_url('http://mobile.zol.com.cn/684/6842718.html','commentsiframe')