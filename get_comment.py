#!/usr/local/bin/python3

from request import content
import soup.attribute as attr
import soup.content as con
import soup.dom as dom
import time
from mysql import insert
from mysql import select
from mysql import update


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
            find_a_list = i.select('.user-name a')
            if not find_a_list:
                return
            find_a = find_a_list[0]
            find_level_list = i.select('.user-level')
            if not find_level_list:
                return
            find_level = find_level_list[0]
            user = attr.Attribute().get_attr(find_a, 'id')
            user_name = con.Content().string_con(find_a)
            comment = con.Content().string_con(i.p)
            level = con.Content().string_con(find_level)
            self.__put_data[times] = {'level': level, 'comment': comment, 'user': user, 'user_name': user_name}
            times += 1
        pass

    def save_data(self):
        data = self.__put_data
        sql = "INSERT INTO comment (user_id,user_name,comment,level,comment_create) VALUES "
        douhao = ''
        for x in data:
            sql += douhao+"('" + str(data[x]['user']) + "','" + str(data[x]['user_name']) + "','" + str(data[x]['comment']).replace('\'','') + "','" + \
                   str(data[x]['level']) + "','" + time.strftime("%Y-%m-%d %H:%M:%S") + "')"
            douhao = ','

        insert.Insert().insert(sql)
        update_sql = "UPDATE iframe_url SET is_used = 1 WHERE iframe_url = '" + self.__comment_url + "'"
        update.Update().update(update_sql)
        pass

if __name__ == '__main__':
    sql = 'SELECT iframe_url,id FROM iframe_url WHERE id > 1456 AND is_used = 0'
    res = select.Select().find_all(sql)
    for x in res:
        url = x[0]
        id = str(x[1])
        if not url or not id:
            continue
        print('id:' + id + 'url:' + url + '开始')
        Comment_page(url)

