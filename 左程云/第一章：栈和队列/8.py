"""
构造数组的MaxTree.首先定义二叉树节点如下：
public class Node{
    public int value;
    public Node left;
    public Node right;
    public Node(int data){
        this.value = data;
    }
}

一个数组的MaxTree定义如下：
1）数组没有重复元素
2）MaxTree是一棵二叉树，数组的每个值对应二叉树一个节点
3）包括MaxTree树在内且在其中的每一棵子树上，值最大的节点都是树的头

要求：给定一个没有重复元素的数组arr，写出生成这个数组的MaxTree函数，
要求时间复杂度为O(N),额外空间复杂度为O(N)

思路：按照下面要求建立的树即满足题目需求
1）每一个数的父节点是它左边第一个比它大的数和它右边第一个比它大的数中，较小的那个
2）如果某个节点左边和右边都没有比它大的数，那么它就是根节点
3）使用单调栈和hashmap可以完成需求
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def MaxTree():
    
