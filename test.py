#!/usr/local/bin/python3

import re
import urllib.parse

str = 'http://power.zol.com.cn/slide/643/6435454_1.html#p=1'


if str.find('http') == -1:
    print(0)