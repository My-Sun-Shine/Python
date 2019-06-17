# 连接MySQL数据库
import mysql.connector

conn = mysql.connector.connect(user="root", password="123456", database="test")
cursor = conn.cursor()  # 获取游标

cursor.execute(
    "create table user(id varchar(20) primary key, name varchar(20), score int)")

cursor.execute("insert into user (id, name, score) values (%s, %s, %s)", (
               'A-001', 'Adam', 95))
print(cursor.rowcount)
conn.commit()
cursor.close()  # 关闭游标
cursor = conn.cursor()
cursor.execute("select * from user where id = %s", ('A-001',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
