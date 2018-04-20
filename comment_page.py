#!/usr/local/bin/python3

import driver.base as base
import soup.dom as dom
import soup.content as con

class Comment_page():

    __comment_url = ''
    __page_source = ''
    __put_data = {}

    def __init__(self,url):
        self.__comment_url = url
        self.get_page_source()
        pass

    def get_page_source(self):
        self.__page_source = base.Base().page_result(self.__comment_url)
        pass

    def get_data(self):
        result = dom.Dom(self.__page_source).soup_result
        select_a = result.find_select('#list_box_new .user-name a')
        for i in select_a:
            self.__put_data