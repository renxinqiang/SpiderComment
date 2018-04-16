#!/usr/local/bin/python3

# from selenium import webdriver
# from bs4 import BeautifulSoup
#
# def driver_result_content(url):
#     driver = webdriver.Firefox()
#     driver.get(url)
#     content = driver.page_source
#     driver.close()
#     return content
#
# def soup_source(html):
#     return BeautifulSoup(content, 'lxml')
#
# home_url = 'http://mobile.zol.com.cn/news/'
#
# # 源码
# content = driver_result_content(home_url)
#
# # 解析
# soup = soup_source(content)
#
# # 查找
# url_list = soup.select('#navswitc-cate a')
#
# for url in url_list:
#     content = driver_result_content(url.get('href'))
#     soup_nex = soup_source(content)
#



from mysql import select

sql = "SELECT * FROM ifram_url";

result = select.Select().result_one(sql)


print(result)



