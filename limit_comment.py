#!/usr/local/bin/python3

import soup,request,config

url_list = config.CONFIG

for url in url_list:
    content = soup.soup_result(request.reques_get(url))
    c = content.find(id='commentsiframe')
    print(c)
    exit()
