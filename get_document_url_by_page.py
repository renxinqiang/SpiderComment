#!/usr/local/python3

from request import content
from soup import dom
from mysql import insert
from mysql import select
import urllib.parse
import re
import config
from selenium import webdriver
import time

class Get_document_url_by_Page():
    __page_url = ''

    def __init__(self, url):
        self.__page_url = url
        self.get_page_data()
        pass

    def get_page_data(self):
        # driverOptions = webdriver.FirefoxOptions()
        # driverOptions.set_headless()
        # driver = webdriver.Firefox(firefox_options=driverOptions)
        # driver.get(self.__page_url)
        # data = driver.page_source
        # driver.close()
        data = content.Content().text(self.__page_url, None)
        a_list = dom.Dom(data).find_select('a')
        if not a_list:
            return
        for i in a_list:
            if 'href' not in str(i):
                continue
            url = i['href']
            if not url:
                continue
            url_path = urllib.parse.urlparse(url).path
            hostname = urllib.parse.urlparse(url).hostname
            data = re.match('\/(slide\/)?\d+\/\d+(_\d+)?\.html', url_path)
            if not data or not hostname:
                continue
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
    # url_list = config.url_list
    # sql = "select document_url,id from document_url where id > 4088 and id <=5000"
    # res = select.Select().find_all(sql)
    # for x in res:
    #     url = x[0]
    #     id = str(x[1])
    #     print('id:'+id+'url:'+url+'开始')
    #     Get_document_url_by_Page(url)

    # sql = "select document_url,id from document_url where id > 7002 and id <= 10000"
    # res = select.Select().find_all(sql)
    # for x in res:
    #     url = x[0]
    #     id = str(x[1])
    #     print('id:' + id + 'url:' + url + '开始')
    #     Get_document_url_by_Page(url)
    #
    sql = "select document_url,id from document_url where id > 19870 and id <= 20000"
    res = select.Select().find_all(sql)
    for x in res:
        url = x[0]
        id = str(x[1])
        print('id:' + id + 'url:' + url + '开始')
        Get_document_url_by_Page(url)
    #
    # sql = "select document_url,id from document_url where id > 15000 and id <= 20000"
    # res = select.Select().find_all(sql)
    # for x in res:
    #     url = x[0]
    #     id = str(x[1])
    #     print('id:' + id + 'url:' + url + '开始')
    #     Get_document_url_by_Page(url)

        # print(x[0])
        # exit()
    # url_list = ['http://geek.zol.com.cn/669/6694213.html']
    # for url in url_list:
    #     Get_document_url_by_Page(url)
    # for x in range(17):
    #     page = x + 1
    #     url = 'http://diy.zol.com.cn/more/2_945_'+str(page)+'.shtml'
    #     Get_document_url_by_Page(url)
    # for x in range(50):
    #     page = x + 1
    #     url = 'http://search.zol.com.cn/s/article_more.php?kword=%CA%D6%BB%FA&page='+str(page)+'&s_cdate=t'
    #     Get_document_url_by_Page(url)
