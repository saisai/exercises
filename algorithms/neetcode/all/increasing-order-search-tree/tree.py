'''
https://www.askpython.com/python/examples/preorder-tree-traversal
https://www.askpython.com/python/examples/inorder-tree-traversal
https://www.askpython.com/python/examples/postorder-tree-traversal-in-python
https://www.askpython.com/python/examples/level-order-binary-tree

'''

from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
root.right = TreeNode(6)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)
'''

def insert(root, val):
    if root is None:
        root = TreeNode(val)
        return root
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

root = insert(None,5)
insert(root, 3)
insert(root, 6)
insert(root, 2)
insert(root, 4)
insert(root, 1)
insert(root, 8)
insert(root, 7)
insert(root, 9)



def preorder(root):
    if root == None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

#preorder(root)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

#inorder(root)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

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

if __name__ == '__main__':
    postorder(root)
    print("\n")
    levelorder(root)


