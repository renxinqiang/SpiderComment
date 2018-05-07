#!/usr/local/bin/python3

for x in range(30):
    url = 'http://dynamic.zol.com.cn/channel/index.php?c=Ajax_MobileData&a=MobileNews&callback=FuncAbstract.setHtml&cid=74&page=' + str(x+1)
    print(url)