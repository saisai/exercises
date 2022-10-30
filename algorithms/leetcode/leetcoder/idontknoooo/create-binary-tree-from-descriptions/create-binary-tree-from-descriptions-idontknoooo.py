'''
https://leetcode.com/problems/create-binary-tree-from-descriptions/
https://leetcode.com/problems/create-binary-tree-from-descriptions/discuss/1824275/python-3-hashmap-on-explanation


Explanation
    Since the tree has only unique value, we can use a dictionary to match value to TreeNode
    Use is_left to decide whether the child is left or right
    Once done that, find root using a set exclusion (minus -) operation
Implementation
'''

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right =right


class S:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        d = dict()
        s = set()
        for par, child, is_left in descriptions:
            s.add(child)
            if par not in d:
                d[par] = TreeNode(par)
            if child not in d:
                d[child] = TreeNode(child)
            if is_left:
                d[par].left = d[child]
            else:
                d[par].right = d[child]
        root = set(d.keys()) - s
        return d[root.pop()]

descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
root = S().createBinaryTree(descriptions)

def preorder(root):
    if root.val == 0:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)


from queue import Queue

def levelorder(root):
    if root == None:
        return
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if node == None:
            continue
        print(node.val)
        q.put(node.left)
        q.put(node.right)

def preorder(root):
    if root == None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)


print("Level order \n")
levelorder(root)

print("Pre order \n")
preorder(root)

print("In order \n")
inorder(root)

print("Post order\n")
postorder(root)




