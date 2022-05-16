from tree import preorder

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.right = right
        self.left = left
        self.next = next


class S:
    def connect(self, root):
        cur, nxt = root, root.left if root else None

        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next =cur.next.left

            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left

        return root


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

root.right = Node(3)
root.right.left=Node(6)
root.right.right=Node(7)

result = S().connect(root)

preorder(result)


