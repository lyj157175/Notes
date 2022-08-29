# 【题目】遍历一颗树的节点
def find_nodes(node, res):
    if not node:
        return

    res.append(node.val)
    find_nodes(node.left, res)
    find_nodes(node.right, res)

    return res


# 【题目】遍历树的所有路径
def find_paths(node, path, paths):
    if not node:
        return

    if not node.left and not node.right:
        paths.append('->'.join([str(node.val) for node in path]))

    path.append(node.left)
    find_paths(node.left, path, paths)
    path.pop()

    path.append(node.right)
    find_paths(node.right, path, paths)
    path.pop()



# 【题目】判断树是不是平衡二叉树（分治法，后序遍历）
def is_balance(root):
    is_balance, _ = helper(root)
    return is_balance

def helper(root):
    if not root:
        return True, 0

    is_balance_left, left_height = helper(root.left)
    is_balance_right, right_height = helper(root.right)
    root_height = max(left_height, right_height) + 1

    if not is_balance_right or not is_balance_left:
        return False, root_height

    if abs(left_height - right_height) > 1:
        return False, root_height

    return True, root_height







