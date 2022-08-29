class V:

    def __init__(self, item):
        self.id = item
        self.nbrs = {}
        self.visited = False
    
    def add_nbr(self, nbr, weight=0):
        self.nbrs[nbr] = weight
    
    def get_nbrs(self):
        return self.nbrs.keys()
    
    def get_idx(self):
        return self.id
    
    def get_weight(self, nbr):
        return self.nbrs[nbr]
    
class Graph:
    
    def __init__(self, directed=False):
        self.v_dict = {}
        self.v_nums = 0
        self.directed = directed
    
    def add_v(self, item):
        new_v = V(item)
        self.v_dict[item] = new_v
        self.v_nums += 1
    
    def get_v(self, item):
        if item in self.v_dict:
            return self.v_dict[item]
        return None
    
    def get_vs(self):
        return self.v_dict.keys()
    
    def add_edge(self, frm, to, weight=0):
        if frm not in self.v_dict:
            self.add_v(frm)
        if to not in self.v_dict:
            self.add_v(to)
        self.v_dict[frm].add_nbr(self.v_dict[to], weight)
        if not self.directed:
            self.v_dict[to].add_nbr(self.v_dict[frm], weight)
    
    def get_edges(self):
        edges = []
        for i, v in self.v_dict.items():
            for nbr in v.get_nbrs():
                edges.append((v.get_idx(), nbr.get_idx(), v.get_weight(nbr)))
        return edges
    
    def get_nbrs(self, item):
        return self.v_dict[item].get_nbrs()


### 遍历
def dfs(G, v, visited):
    visited[v] = True
    for nbr in v.get_nbrs():
        if nbr not in visited:
            dfs(G, nbr, visited)
    return 

def DFS_transvel(G):
    visited = {}
    for v in G:
        if v not in visited:
            dfs(G, v, visited)
    


def bfs(graph, v):
    queue = []
    visited = set()
    queue.append(v)
    visited.add(v)

    while len(queue) > 0:
        node = queue.pop()
        nbrs = graph(node)
        for nbr in nbrs:
            if nbr not in visited:
                queue.append(nbr)
                visited.add(nbr)
        print(node)














