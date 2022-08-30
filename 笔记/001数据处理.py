# -------------------- csv文件的读写 ---------------------------
import pandas as pd

file_path = '一级市场公司标的归一词.xlsx'
data = pd.read_excel(file_path)

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


