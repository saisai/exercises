
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class S:
    def maxDepth(self, root):
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
        
        return depth


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(S().maxDepth(root))

