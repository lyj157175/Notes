import re

# ----------------------------------- 正则 ---------------------------------
# . 匹配任意单个字符
# * 表示任意个字符（包括0个字符）
# ^不取消
reg = '.*减持.*股份.*|.*减持.*|.*拟.*减持.*^取消.*'
text = '最近公司开始减持大量的股份'
res = re.match(reg, text)
print(res)


text = 'xxxxxxxxx文案xxxx'
rex = '^((?!取消).)*今天((?!取消).)*$'
rex = '.*你好.*我们.*|^((?!取消).)*今天.*会议((?!取消).)*$'   # 出现（今天&&会议&&！取消）
res = re.match(rex, text)
print(res)


content = 'xxxx你好xxxx谢谢xxxxxx大家xxxxx'
reg = '.*(你好|今天).*(上午|谢谢).*(大家|来吧).*'    # |代表或者的概念，之间有顺序
res = re.match(reg, content)
print(res)


# 替换操作replace
text = "基于\"此经\"营的“祺CH'IN”品牌\'采"
text = text.replace('\"', '')
text = text.replace('\'', '')
print(text)

