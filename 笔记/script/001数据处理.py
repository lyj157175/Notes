# -------------------- csv文件的读入 ---------------------------
import pandas as pd

file_path = '公司标的.xlsx'
data = pd.read_excel(file_path)
# data = pd.read_excel(file_path, encoding='utf-8')


### ------------------- pandas的test ---------------------------
# print(data)    # 打印全表
# print(data.组织机构)   # 打印某表头的列
# print(data.iloc[:, :3])    # 打印具体的几行几列
# print(data.index.values)    # 获取行数为list，不包括表头
# print(data.columns.values)   # 获取表头为list
# print(data.loc[0].values)    # 打印第零行的数据为list
# print(data.iloc[0,1])  # 读取某行某列的值
# -------------------------------------------------------------

match_dict = set()
for id in data.index.values :
    line = data.loc[id].values
    print(id)
    print(line)


# ---------------------------  数据的写入 ------------------------------------
import pandas as pd
data = []

header = ['content']
dt = pd.DataFrame(data, columns=header)
dt.to_excel("news_test.xlsx", index=0, sheet_name='event')   # 可以用for遍历来指定sheet_name
