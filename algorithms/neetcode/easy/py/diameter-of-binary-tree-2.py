
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class S:
    
    def diameterOfBinaryTree(self, root):
        lp = 0
        stack = [[root, False]]
        heights = {}
        while stack:
            node, seen = stack[-1]
            if not seen:
                stack[-1][1] = True
                if node.left:
                    stack.append([node.left, False])
                if node.right:
                    stack.append([node.right, False])
            else:
                left = heights.get(node.left, 0)
                right = heights.get(node.right, 0)
                if left + right > lp:
                    lp = left + right
                heights[node] = max(left, right) + 1
                stack.pop()
        return lp

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)

print(S().diameterOfBinaryTree(root))

https://leetcode.com/problems/diameter-of-binary-tree/discuss/1973394/Iterative-Python-Solution-or-O(N)-or-Beats-99.52-Memory

