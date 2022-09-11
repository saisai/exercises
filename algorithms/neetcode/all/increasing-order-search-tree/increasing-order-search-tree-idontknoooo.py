'''
https://leetcode.com/problems/increasing-order-search-tree/
https://leetcode.com/problems/increasing-order-search-tree/discuss/1955004/python-3-iterative-in-order-traversal-explanation

Explanation
    Perform an in-order traversal
    Let the right child of the previous/smaller node be the current node
    Remove the left child to avoid cycle
    Return the smallest node

Implementation

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class S:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        node = root
        stack = []
        prev = None
        lowest = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if not lowest:
                    lowest = node
                node.left = None
                if prev:
                    prev.right = node
                prev = node
                node = node.right
        return lowest

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
root.right = TreeNode(6)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)

result = S().increasingBST(root)
print(result)




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

inorder(result)
print("\n")
preorder(result)


