import re

# ----------------------------------- 正则 ---------------------------------
# . 匹配任意单个字符
# * 表示任意个字符（包括0个字符）
# ^不取消
reg = '.*减持.*股份.*|.*减持.*|.*拟.*减持.*^取消.*'
text = '最近公司开始减持大量的股份'
res = re.match(reg, text)
print(res)



# 替换操作replace
text = "基于\"此经\"营的“祺CH'IN”品牌\'采"
text = text.replace('\"', '')
text = text.replace('\'', '')
print(text)

