# SQLite是一种嵌入式数据库，它的数据库就是一个文件
# 由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成
# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用
import os
import sqlite3

db_file = os.path.join(os.path.dirname(__file__), "test.db")
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)  # 连接数据库
cursor = conn.cursor()  # 获取游标，通过游标执行sql语句
cursor.execute(
    'create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    '返回指定分数区间的名称，按分数从低到高排序'
    try:
        # query_str = "select name from user where score>=" + \
        #     str(low)+" and score<="+str(high)+" order by score"
        query_str = r"select name from user where score>=? and score<=? order by score"
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        results = cursor.execute(query_str, (low, high)).fetchall()
        #results = cursor.execute(query_str).fetchall()
        #results = cursor.execute("select name from user where score>=80 and score <=95 order by score desc").fetchall()
        return [result[0] for result in results]
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


print(get_score_in(80, 95))
print(get_score_in(60, 80))
print(get_score_in(60, 100))
