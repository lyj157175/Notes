# 图的实现确定一种即可

class Edge:
    def __init__(self, weight, from_, to_):   # from_, to_都是Node类型
        self.weight = weight
        self.from_ = from_
        self.to_ = to_

class Node:
    def __init__(self, val):
        self.val = val
        self.in_ = 0   # 入度
        self.out_ = 0  #出度
        self.nexts = []  # 出度连的节点
        self.edges = []  # 出度连接的边


class Graph:
    def __init__(self):
        self.nodes = {}    
        self.edges = set()


