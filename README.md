# 评论抓取

* python3
* mysql5.6.27
* PyCharm 2017.3.2 

# 目录
```
├── README.md
├── config
│   ├── __init__.py   
│   └── __pycache__
├── driver
│   ├── __init__.py
│   ├── __pycache__
│   ├── base.py
│   ├── element.py
│   ├── execute.py
│   └── script.py
├── geckodriver.log
├── get_comment.py
├── get_document_url_by_json.py
├── get_document_url_by_page.py
├── get_iframe_url.py
├── log
│   ├── __init__.py
│   └── __pycache__
├── mysql
│   ├── __init__.py
│   ├── __pycache__
│   ├── delete.py
│   ├── insert.py
│   ├── select.py
│   └── update.py
├── request
│   ├── __init__.py
│   ├── __pycache__
│   ├── content.py
│   ├── cookie.py
│   └── uri.py
├── soup
│   ├── __init__.py
│   ├── __pycache__
│   ├── attribute.py
│   ├── content.py
│   └── dom.py
└── test.py
```
### 广度优先抓取模式

### 抓取流程
1. 文章链接
2. 评论iframe链接抓取
3. 评论页评论抓取

### 抓取过程中的坑
* 仔细分析ZOL文章之后,iframe链接有两种,一种是组图页,一种是普通文章页
使用request通过组图文章进入评论页时会遇到被屏蔽的情况,一开始使用selenium模拟登入页面抓取里面评论分页链接,能够得到想要结果,但是效率极差,并且会遇到
超时情况,一个组图文章到抓取评论iframe链接平均需要5S左右时间,这个时间对于上万文章链接处理,实在是太慢了,无法忍受.加以研究组图链接后,发现可以剔除
链接中slide和_X就可以将组图文章转换成普通文章,这样使用request抓取页面内容beautifulsoup解析内容 效果非常理想
* mysql编码设置,之前没有设置编码的时候可以处理,但是后期加编码时卡在了utf-8上,调试不通啊,网上也没有相应案例,看报错也是编码问题,偶然改成utf8,世界
安静了.还是天助我也.......
