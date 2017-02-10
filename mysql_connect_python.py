# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:11:14 2017
使用python连接MYSQL，connect像路，corso类似卡车
@author: yyh
"""

import MySQLdb
conn=MySQLdb.connect(
                     host='localhost',
                     port=3306,
                     user='root',
                     passwd='root',
                     db='world',
                     charset='utf8'
                     )
cursor=conn.cursor()
sql_insert='insert into customers(cust_id,cust_name) values('1000000009','nihao')'
sql_update='update customers set cust_name='nihao' where cust_id='1000000005''
sql_delete='delete from customers where cust_name='Fun4All''
try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount
    
except Exception as e:
    print e
    conn.rollback
#print conn,cursor
#sql='select * from customers'
#cursor.execute(sql)
#rs=cursor.fetchone()
#print rs
#rs=cursor.fetchmany(3)
#print rs
#rs=cursor.fetchall()
#for i in rs:
#print i

conn.close()
cursor.close()
