import pymysql
import time
import datetime



db = pymysql.connect(
    host="172.18.128.127",
    port=3306,
    user='root',
    password='123456',
    charset='utf8mb4',
    database='cls_data'  # 连接的数据库
    )

cursor = db.cursor()
cursor.execute('show databases')


try:
    t1 = time.time()
    time_gap = ((datetime.datetime.now()) + datetime.timedelta(days=-26)).strftime("%Y-%m-%d %H:%M:%S")
    now = int(time.time())

    sql = "select event_content, publish_time from event_extract_history " \
          "where publish_time > '{time}' and event_subject = '{query}' order by publish_time".format(time=str(now - 259200),
                                                                                                        query='xxx')
    cursor.execute(sql)
    mysql_results = cursor.fetchall()  ### fetchone(), fetchmany(), fetchall()

    for line in mysql_results:
        print(line[0], line[1])

    print('数据长度', len(mysql_results))
    print('用时', time.time()-t1)


except:
    print ("Error: unable to fetch data_csv")


##### pymysql完成插入操作
# try:
#     sql = "insert into lyj1(id, title, content) values(10, 'xxx', 'rrr')"
#     cursor.execute(sql)
#     db.commit()

# except Exception as e:
#     print(str(e))
#     db.rollback()  #回滚事务


cursor.close()
db.close()


# --------------------------------------------- 线程池连接 -----------------------------------
### pip isntall DBUtils==1.2
# from DBUtils.PooledDB import PooledDB
#
# pool = PooledDB(
#     creator=pymysql,
#     mincached=5,  # 最少连接数
#     host='172.18.128.127',
#     port=3306,
#     user='root',
#     passwd='123456',
#     database='cls_data',
#     charset='utf8mb4',
#     setsession=['SET AUTOCOMMIT = 1']  # 自动更新配置是否打开
# )
# conn = pool.connection()
# cursor = conn.cursor()





################### docker创建mysql及连接 ####################################
# 1.在lyj_mysql目录下：
# mkdir -p /user/yuanie/lyj_mysql/conf
# mkdir -p /user/yuanie/lyj_mysql/data
# mkdir -p /user/yuanie/lyj_mysql/logs

# 2.在conf 目录下配置mysqld.cnf 文件
# vim mysqld.cnf
# # 输入以下内容，并保存退出
# [client]
# default-character-set=utf8
# [mysqld]
# character-set-server=utf8
# collation-server=utf8_general_ci

# 3.docker启动容器
# docker run
# --name lyj_mysql
# -p 3306:3306
# -v /user/yuanjie/lyj_mysql/conf:/etc/mysql/mysql.conf.d
# -v /user/yuanjie/lyj_mysql/data:/var/lib/mysql
# -v /user/yuanjie/lyj_mysql/logs:/logs
# -e MYSQL_ROOT_PASSWORD=123456
# -d mysql

# 4.进入容器
# docker exec -it lyj_mysql /bin/bash

# 5.登录mysql
# mysql -uroot -p
# 输入password




# ---------------------------------- mysql语法学习 ----------------------------------------------
# 插入
# insert into lyj1(id, title, content) values(3, 'insert111111', 'insert content');


# join语法
sql = 'select * from table_a, table_b where table_a.id = table_b.id'


# 查看mysql的子查询
# sql = 'select content from news_realtime where item_id in (select news_id from news_data where event_id = "fdfzozbeaqtrpqpel60")
