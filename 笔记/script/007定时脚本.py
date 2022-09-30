import schedule
import time
import datetime

# 定义你要周期运行的函数
def job():
    print("I'm working...")





if __name__ == '__main__':
    schedule.every(10).minutes.do(job)               # 每隔 10 分钟运行一次 job 函数
    schedule.every().hour.do(job)                    # 每隔 1 小时运行一次 job 函数
    schedule.every().day.at("10:30").do(job)         # 每天在 10:30 时间点运行 job 函数
    schedule.every().monday.do(job)                  # 每周一 运行一次 job 函数
    schedule.every().wednesday.at("13:15").do(job)   # 每周三 13：15 时间点运行 job 函数
    schedule.every().minute.at(":17").do(job)        # 每分钟的 17 秒时间点运行 job 函数

    print('当前时间:', (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S"))
    print('10天前时间', ((datetime.datetime.now()) + datetime.timedelta(days=-10)).strftime("%Y-%m-%d %H:%M:%S"))

    
    while True:
        schedule.run_pending()   # 运行所有可以运行的任务
        time.sleep(1)