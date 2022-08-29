# 适用场景：分层遍历，连通块问题，拓扑排序

# bfs三种实现方式：单队列，双队列，dummynode

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

