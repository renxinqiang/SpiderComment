#!/usr/local/bin/python3

from request import content
from selenium import webdriver
import soup.dom as dom
import soup.attribute as attr
from mysql import insert
from mysql import select
from mysql import update


class Get_iframe_url():

    __comment_url = ''

    __doc_url = ''

    __page_source = ''

    __put_data = []

    __comment_host = 'http://comment.zol.com.cn'

    __iframe_id = ''

    __css = ''

    def __init__(self,url,type,css='.more-comments a'):
        self.__iframe_id = type
        self.__doc_url = url
        self.__css = css
        self.get_page_source()
        self.set_data()
        self.save_data()
        pass

    def get_page_source(self):
        if self.__iframe_id == 'commentsIframe':
            driverOptions = webdriver.FirefoxOptions()
            driverOptions.set_headless()
            driver = webdriver.Firefox(firefox_options=driverOptions)
            driver.get(self.__doc_url)
            driver.switch_to.frame(self.__iframe_id)
            css_html = driver.find_element_by_css_selector(self.__css)
            if not css_html:
                driver.close()
                return
            self.__comment_url = css_html.get_attribute('href')
            driver.close()
            self.__page_source = content.Content().text(self.__comment_url, None)
        else:
            data = content.Content().text(self.__doc_url, None)
            url = None
            iframe = dom.Dom(data).find_select('iframe')
            if iframe:
                url = iframe[0]['src']
            else:
                i = dom.Dom(data).find_select('script')
                for x in i:
                    x = str(x)
                    res = x.replace('\n','')
                    if 'comment.zol.com.cn' not in res:
                        continue
                    k = res.split(' ')
                    for xx in k:
                        if 'comment.zol.com.cn' in xx:
                            url = xx.replace('"', '\'')
                            url = url.replace('\'//', 'http://')
                            url = url.replace('\';', '')
                            url = url.replace('}', '')
                            url = url.replace('\'', '')
                            break
            if not url:
                return
            iframe_url = content.Content().text(url, None)
            iframe_url_more = dom.Dom(iframe_url).find_select(self.__css)
            if not iframe_url_more:
                return
            iframe_url_first = iframe_url_more[0]
            self.__comment_url = iframe_url_first['href']
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
            insert.Insert().close_connect()

        update_sql = "UPDATE document_url SET is_used = 1 WHERE document_url = '" + self.__doc_url + "'"
        update.Update().update(update_sql)
        update.Update().close_connect()
        pass


if __name__ == '__main__':
    sql = "select document_url,id,iframe_id from document_url where id > 6767 and is_used = 0"
    # sql = "select document_url,id,iframe_id from document_url where document_url = 'http://mobile.zol.com.cn/645/6451596.html'"
    res = select.Select().find_all(sql)
    for x in res:
        url = x[0]
        iframe_id = x[2]
        # if iframe_id == 'commentsIframe':
        #     continue
        id = str(x[1])
        print('id:' + id + 'url:' + url + 'iframe_id:' + iframe_id + '开始')
        if id == '6792':
            Get_iframe_url(url,iframe_id,'.detail-side-list .review-all')
        else:
            Get_iframe_url(url, iframe_id)