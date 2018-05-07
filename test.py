#!/usr/local/bin/python3

import re
import urllib.parse

str = 'http://power.zol.com.cn/slide/643/6435454_1.html#p=1'
url_path = urllib.parse.urlparse(str).path

data = re.match('\/(slide\/)?\d+\/\d+(_\d+)?\.html',url_path)
if not data:
    print(11111)
print(data)