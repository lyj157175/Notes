class Node:
    
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right
    

class BST:

    def __init__(self, root=None):
        self.root = root
    
    
    def get(self, key):
        return self._get(self.root, key)
    
    def _get(self, node, key):
        if node is None:
            return None  
        if key < node.val:
            return self._get(node.left, key)
        elif key > node.val:
            return self._get(node.right, key)
        else:
            return node
    

    def add(self, key):
        self.root = self._add(self.root, key)
    
    def _add(self, node, key):
        if node is None:
            return Node(key)
        if key == node.val:
            pass
        else:
            if key < node.val:
                node.left = self._add(node.left, key)
            elif key > node.val:
                node.right = self._add(node.right, key)
        return node


    def remove(self, key):
        self.root = self._remove(self.root, key)
    
    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.val:
            node.left = self._remove(node.left, key)
        elif key > node.val:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                node.val = self.get_max(node.right)
                node.right = self._remove(node.right, node.val)
        return node
    

    def get_max(self, node):
        if node is None:
            return None
        while node.right:
            node = node.right
        return node.val
    
    def inorder(self):
        self._print_inorder(self.root)
    
    def _print_inorder(self, node):
        if node is None:
            return 
        self._print_inorder(node.left)
        print(node.val, end=' ')
        self._print_inorder(node.right)
    
    def preorder(self):
        self._print_preorder(self.root)
    
    def _print_preorder(self, node):
        if node is None:
            return 
        print(node.val, end=' ')
        self._print_preorder(node.left)
        self._print_preorder(node.right)
    
    def postorder(self):
        self._print_postorder(self.root)
    
    def _print_postorder(self, node):
        if node is None:
            return 
        self._print_postorder(node.left)
        self._print_postorder(node.right)
        print(node.val, end=' ')


     







