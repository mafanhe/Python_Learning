import MySQLdb

conn = MySQLdb.Connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='bxxt',charset='utf8')
cursor = conn.cursor()
sql_insert = "insert into pub_bxfj(bxbh,fjwjm) values(20,'insrt_test')"
sql_update = "update pub_bxfj set fjwjm='update_test' where bxhb=20"
sql_delete = "delete from pub_bxfj where bxbh=20"

cursor.execute(sql_insert)
print cursor.rowcount
cursor.execute(sql_update)
print cursor.rowcount
cursor.execute(sql_delete)
print cursor.rowcount


cursor.close()
conn.close()
