#!/usr/local/bin/python3

from mysql import select
from mysql import update

sql = "select * from document_url where is_used = 0"

list1 = select.Select().find_all(sql)
for x in list1:
    id = x[0]
    url = x[1].replace('slide/','').replace('_1','')
    up_sql = "update document_url set document_url = '" + url + "',iframe_id = 'commentsiframe' where id = " + str(id)
    update.Update().update(up_sql)