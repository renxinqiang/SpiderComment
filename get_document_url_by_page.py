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
            if 'href' not in str(i):
                continue
            url = i['href']
            if not url:
                continue
            url_path = urllib.parse.urlparse(url).path
            data = re.match('\/(slide\/)?\d+\/\d+(_\d+)?\.html', url_path)
            if not data:
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
    # url_list = ['http://mobile.zol.com.cn/', 'http://mobile.zol.com.cn/iphone.html', 'http://mobile.zol.com.cn/soc/',
    #             'http://4g.zol.com.cn/', 'http://5g.zol.com.cn/', 'http://smartwear.zol.com.cn/',
    #             'http://mobile.zol.com.cn/chaiji.html']
    # url_list = ['http://nb.zol.com.cn/yxb/',
    #             'http://pad.zol.com.cn/',
    #             'http://pc.zol.com.cn/',
    #             'http://aio.zol.com.cn/',
    #             'http://robot.zol.com.cn/',
    #             'http://nb.zol.com.cn/portable.html',
    #             'http://lcd.zol.com.cn/vr.html']
    # url_list = ['http://diy.zol.com.cn/',
    #             'http://cpu.zol.com.cn/',
    #             'http://vga.zol.com.cn/',
    #             'http://lcd.zol.com.cn/',
    #             'http://mouse.zol.com.cn/',
    #             'http://mb.zol.com.cn/',
    #             'http://ssd.zol.com.cn/',
    #             'http://memory.zol.com.cn/',
    #             'http://bi.zol.com.cn/',
    #             'http://power.zol.com.cn/',
    #             'http://esports.zol.com.cn/']
    # url_list = ['http://dcdv.zol.com.cn/',
    #             'http://lasertv.zol.com.cn/',
    #             'http://sound.zol.com.cn/',
    #             'http://headphone.zol.com.cn/',
    #             'http://mouse.zol.com.cn/',
    #             'http://display.zol.com.cn/',
    #             'http://dcdv.zol.com.cn/travel.html',
    #             'http://oled.zol.com.cn/']
    # url_list = ['http://jd.zol.com.cn/',
    #             'http://tv.zol.com.cn/',
    #             'http://icebox.zol.com.cn/',
    #             'http://life.zol.com.cn/',
    #             'http://washer.zol.com.cn/',
    #             'http://ac.zol.com.cn/',
    #             'http://jd.zol.com.cn/category_52.html',
    #             'http://hd.zol.com.cn/',
    #             'http://air.zol.com.cn/',
    #             'http://water.zol.com.cn/',
    #             'http://sh.zol.com.cn/']
    # url_list = ['http://biz.zol.com.cn/',
    #             'http://oa.zol.com.cn/',
    #             'http://oa.zol.com.cn/printer.html',
    #             'http://projector.zol.com.cn/',
    #             'http://net.zol.com.cn/',
    #             'http://projector.zol.com.cn/movie.html',
    #             'http://server.zol.com.cn/',
    #             'http://teach.zol.com.cn/',
    #             'http://health.zol.com.cn/',
    #             'http://cloud.zol.com.cn/']
    url_list = ['http://auto.zol.com.cn/',
                'http://geek.zol.com.cn/',
                'http://ebike.zol.com.cn/',
                'http://ai.zol.com.cn/',
                'http://gps.zol.com.cn/',
                'http://3dp.zol.com.cn/',
                'http://chepin.zol.com.cn/',
                'http://lock.zol.com.cn/']
    for url in url_list:
        Get_document_url_by_Page(url)
    # for x in range(17):
    #     page = x + 1
    #     url = 'http://diy.zol.com.cn/more/2_945_'+str(page)+'.shtml'
    #     Get_document_url_by_Page(url)
    # for x in range(5):
    #     page = x + 1
    #     url = 'http://nb.zol.com.cn/detail_13271/p_'+str(page)+'/'
    #     Get_document_url_by_Page(url)
