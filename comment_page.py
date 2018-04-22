#!/usr/local/bin/python3

from request import content
import soup.attribute as attr
import soup.content as con
import soup.dom as dom
import time
from mysql import insert


class Comment_page():
    __comment_url = ''
    __page_source = ''
    __put_data = {}

    def __init__(self, url):
        self.__comment_url = url
        self.get_page_source()
        self.get_data()
        self.save_data()
        pass

    def get_page_source(self):
        self.__page_source = content.Content().text(self.__comment_url, None)
        pass

    def get_data(self):
        select_li = dom.Dom(self.__page_source).find_select('#list_box_new li')
        times = 0
        for i in select_li:
            find_a = i.select('.user-name a')[0]
            find_level = i.select('.user-level')[0]
            user = attr.Attribute().get_attr(find_a, 'id')
            user_name = con.Content().string_con(find_a)
            comment = con.Content().string_con(i.p)
            level = con.Content().string_con(find_level)
            self.__put_data[times] = {'level': level, 'comment': comment, 'user': user, 'user_name': user_name}
            times += 1
        pass

    def save_data(self):
        data = self.__put_data
        for x in data:
            sql = "INSERT INTO comment (user_id,user_name,comment,level,comment_create)" \
                  "VALUES ('" + str(data[x]['user']) + "','" + str(data[x]['user_name']) + "','" + str(data[x]['comment']) + "','" + \
                   str(data[x]['level']) + "','" + time.strftime("%Y-%m-%d %H:%M:%S") + "')";
            insert.Insert().insert(sql)
        pass

if __name__ == '__main__':
    Comment_page('http://comment.zol.com.cn/22/6860066_0_0_1.html')
