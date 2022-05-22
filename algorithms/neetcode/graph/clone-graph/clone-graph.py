
class Node:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class S:
    def cloneGraph(self, node):
        oldToNew = {}
        def dfs(node):            
            print(node.val)
            if node is oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy      
        return dfs(node) if node else None


n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbors.append(n2)
n1.neighbors.append(n4)
n2.neighbors.append(n1)
n2.neighbors.append(n3)
n3.neighbors.append(n2)
n3.neighbors.append(n4)
n4.neighbors.append(n1)
n4.neighbors.append(n3)
result = S().cloneGraph(n1)

# https://www.youtube.com/watch?v=mQeF6bN8hMk&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=6&ab_channel=NeetCode

