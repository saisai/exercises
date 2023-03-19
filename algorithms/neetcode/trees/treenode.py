
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
    """ Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
    """

    def height(self, node):
        if node is None:
            return 0
        else:
            # Compute the height of each sub tree
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            # Use the larger one
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def printCurrentLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.val, end= " ")
        elif level > 1:
            self.printCurrentLevel(root.left, level - 1)
            self.printCurrentLevel(root.right, level - 1)

    def printLevelOrder(self, root):
        h = self.height(root)
        for i in range(1, h + 1):
            self.printCurrentLevel(root, i)

    '''
    Algorithm Postorder(tree)

    Traverse the left subtree, i.e., call Postorder(left->subtree)
    Traverse the right subtree, i.e., call Postorder(right->subtree)
    Visit the root
    '''

    def printPostorder(self, root):
        if root:
            # first recur on left child
            self.printPostorder(root.left)

            # recurn on right child
            self.printPostorder(root.right)

            # print the val of node
            print(root.val, end=" ")

    '''
    Algorithm Preorder(tree)

    Visit the root.
    Traverse the left subtree, i.e., call Preorder(left->subtree)
    Traverse the right subtree, i.e., call Preorder(right->subtree) 
    '''

    def printPreorder(self, root):
        if root:

            print(root.val, end=" ")

            # recur on left child
            self.printPreorder(root.left)

            # recur on right child
            self.printPreorder(root.right)


    '''
    Traverse the left subtree, i.e., call Inorder(left->subtree)
    Visit the root.
    Traverse the right subtree, i.e., call Inorder(right->subtree)

    '''
    def printInorder(self, root):
        if root:
            # recur on left child
            self.printInorder(root.left)

            print(root.val, end=" ")

            # recur on right child
            self.printInorder(root.right)



# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# https://www.geeksforgeeks.org/level-order-tree-traversal/
