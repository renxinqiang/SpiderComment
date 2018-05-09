#!/usr/local/python3

from request import content
from mysql import insert
from mysql import select

import json

class Get_document_url_by_json():
    __json_url = ''

    def __init__(self, url):
        self.__json_url = url
        self.get_json_data()
        pass

    def get_json_data(self):
        data = content.Content().content(self.__json_url, None)
        data = data.replace('FuncAbstract.setHtml(', '')
        data = data.replace(')', '')
        json_str = json.loads(data)
        title_res = json_str
        for i in title_res:
            url = i['url']
            iframe_id = 'commentsiframe'
            if 'slide' in url:
                iframe_id = 'commentsIframe'

            select_sql = "select * from document_url where document_url = '" + url + "'"
            res = select.Select().find_one(select_sql)
            if res:
                continue

            sql = "INSERT INTO document_url (document_url,iframe_id)" \
                  "VALUES ('" + url + "','"+ iframe_id +"')"
            insert.Insert().insert(sql)
            pass

if __name__ == '__main__':
    for x in range(107):
        page = x + 2
        # url = 'http://dynamic.zol.com.cn/channel/index.php?c=Ajax_MobileData&a=MobileNews&callback=FuncAbstract.setHtml&cid=74&page=' + str(page)
        # url = 'http://dynamic.zol.com.cn/channel/index.php?c=Ajax_MobileData&a=MobileNews&callback=FuncAbstract.setHtml&cid=392&page=' + str(page)
        url = 'http://labs.zol.com.cn/router.php?c=TestChannel_Default&a=GetChannelNew&module=new&page=' + str(page)
        Get_document_url_by_json(url)
