import pymysql
import time
import datetime



db = pymysql.connect(
    host="172.18.128.119",
    port=3306,
    user='root',
    password='123456',
    charset='utf8mb4',
    database='lyj_data'  # 连接的数据库
    )

cursor = db.cursor()
cursor.execute('show databases')


try:
    for i in range(1000):
        id = i
        print(i)
        sql = "insert into lyj1(id, title, content) values('{i}', '{t}', '{c}')".format(i=i, t='xxx', c='fff')
        cursor.execute(sql)
        db.commit()
    print('sucessed!')

except Exception as e:
    print(str(e))
    db.rollback()  #回滚事务

cursor.close()
db.close()