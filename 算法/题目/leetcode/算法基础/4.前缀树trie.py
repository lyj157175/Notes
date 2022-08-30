# 前缀树trie也叫字典树， 是N叉树的一种特殊形式。通常来说，一个前缀树是用来存储字符串的。
# 前缀树的一个重要的特性是，节点所有的后代都与该节点相关的字符串有着共同的前缀。
# https://blog.csdn.net/weixin_40274123/article/details/94026945

class Node:
    def __init__(self):
        self.pass_ = 0   # 记录经过当前节点的次数
        self.end_ = 0    # 记录字符串结尾时，加1
        self.map = [None for i in range(26)]   # 每个节点都有26条路
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        if word is None:
            return 

        node = self.root
        for i in word:
            index = ord(i) - ord('a') # ord计算ASCII，计算当前字符的数字表示
            if node.map[index] == None:
                node.map[index] = node()   # 增加一个节点
            node = node.map[index]
            node.pass_+=1
        node.end_ += 1
        print('insert successful !')

    def search(self, word):
        if word == None:
            return 0
        
        node = self.root
        for i in word:
            index = ord(i) - ord('a')
            if node.map[index] == None:  # for循环走不完说明树中没有此字符串
                return 0
            node = node.map[index]
        return node.end_    # 返回字符串出现的次数
    
    def delete(self, word):
        if self.search(word) != 0:  # 存在需要删除的字符串
            node = self.root
            for i in word:
                index = ord(i) - ord('a')
                node.map[index].path -= 1
                if node.map[index].path == 0:  # 如果没有pass_值直接删除节点
                    node.map[index] = None
                    return
                node = node.map[index]
            node.end_ -= 1
    

    def prefix_num(self, pre):
        if pre == None:
            return 0
        node = self.root
        for i in pre:
            index = ord(i) - ord('a')
            if node.map[index] == None:
                return 0
            node = node.map[index]
        return node.pass_


