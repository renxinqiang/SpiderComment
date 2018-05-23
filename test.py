#!/usr/local/bin/python3

from mysql import select
from mysql import update

sql = "select * from document_url where document_url like '//%'"

list1 = select.Select().find_all(sql)
print(list1)
# for x in list1:
#     id = x[0]
#     url = 'http:'+x[1]
#     up_sql = "update document_url set document_url = '" + url + "' where id = " + str(id)
#     update.Update().update(up_sql)