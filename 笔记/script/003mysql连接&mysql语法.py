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
    # sql = "select id, title, content, publish_time from news_offline_2022 " \
    #       "where publish_time > '{time}' and content like '{query}' order by publish_time".format(time=time_gap, query='%' + query + '%')

    sql = "select event_content, publish_time from event_extract_history " \
          "where publish_time > '{time}' and event_subject = '{query}' order by publish_time".format(time=str(now - 259200),
                                                                                                        query='xxx')

    cursor.execute(sql)
    mysql_results = cursor.fetchall()  ### fetchone(), fetchmany(), fetchall()

    for line in mysql_results:
        print(line[0])
        print(line[1])


    print('数据长度', len(mysql_results))
    print('用时', time.time()-t1)


except:
    print ("Error: unable to fetch data_csv")


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





# ----------------------------- mysql语法 ----------------------------------------------
# join语法
sql = 'select * from table_a, table_b where table_a.id = table_b.id'


# 查看mysql的子查询
# sql = 'select content from news_realtime where item_id in (select news_id from news_data where event_id = "fdfzozbeaqtrpqpel60")