# bfs适用场景：分层遍历，连通块问题，拓扑排序
# 可以在树和图上进行
# bfs三种实现方式：单队列，双队列，dummynode

# 图 -> 树（无环的图） -> 二叉树


# 【题目】二叉树的层遍历
def tree_ceng_order(root):
    if not root: return []

    queue, res = [root], []

    while queue:
        res.append([node.val for node in queue])
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

    return res




# 树和图的bfs的通用模板
def find_nodes_bfs(node):
    queue = [node]
    visited = set([node])
    while queue:
        node = queue.pop(0)

        for neighbor in node.get_neighbor():
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
    return list(visited)


