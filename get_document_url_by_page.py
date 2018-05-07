#!/usr/local/python3

from request import content
from soup import dom
from mysql import insert

class Get_document_url_by_Page():
    __page_url = ''

    def __init__(self, url):
        self.__page_url = url
        self.get_page_data()
        pass

    def get_page_data(self):
        data = content.Content().text(self.__page_url, None)
        a_list = dom.Dom(data).find_select('.info-head a')

        if not a_list:
            return
        for i in a_list:
            url = i['href']
            iframe_id = 'commentsiframe'
            if url.find('slide') != -1:
                iframe_id = 'commentsIframe'

            sql = "INSERT INTO document_url (document_url,iframe_id)" \
                  "VALUES ('" + url + "','"+ iframe_id +"')"
            insert.Insert().insert(sql)
            pass

if __name__ == '__main__':
    # url = 'http://4g.zol.com.cn/more/2_1298_3.shtml'
    # Get_document_url_by_Page(url)
    for x in range(2):
        page = x + 1
        url = 'http://4g.zol.com.cn/more/2_1301_'+str(page)+'.shtml'
        Get_document_url_by_Page(url)
