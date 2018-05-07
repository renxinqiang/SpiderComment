#!/usr/local/python3

from request import content
from soup import dom
from mysql import insert
from mysql import select
import urllib.parse
import re

class Get_document_url_by_Page():
    __page_url = ''

    def __init__(self, url):
        self.__page_url = url
        self.get_page_data()
        pass

    def get_page_data(self):
        data = content.Content().text(self.__page_url, None)
        a_list = dom.Dom(data).find_select('a')

        if not a_list:
            return
        for i in a_list:
            url = i['href']
            url_path = urllib.parse.urlparse(url).path
            data = re.match('\/(slide\/)?\d+\/\d+(_\d+)?\.html', url_path)
            if not data:
                continue
            iframe_id = 'commentsiframe'
            if url.find('slide') != -1:
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
    url = 'http://diy.zol.com.cn/'
    Get_document_url_by_Page(url)
    # for x in range(17):
    #     page = x + 1
    #     url = 'http://diy.zol.com.cn/more/2_945_'+str(page)+'.shtml'
    #     Get_document_url_by_Page(url)
    # for x in range(5):
    #     page = x + 1
    #     url = 'http://nb.zol.com.cn/detail_13271/p_'+str(page)+'/'
    #     Get_document_url_by_Page(url)
