
class Node:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class S:
    def cloneGraph(self, node):
        if not node:
            return None
        prev = { node.val: node }
        curr = { node.val: Node(val=node.val) }
        val = node.val
        queue = [node]
        while queue:
            node = queue.pop(0)
            if node.val not in prev:
                prev[node.val] = node
            if node.val not in curr:
                curr[node.val] = Node(val=node.val)

            for n in node.neighbors:
                if n.val not in prev:
                    queue.append(n)
        for t in prev.keys():
            nw = curr[t]
            for nbr in prev[t].neighbors:
                nw.neighbors.append(curr[nbr.val])
        return curr[val]
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbors.append(n2)
n1.neighbors.append(n4)
n2.neighbors.append(n1)
n2.neighbors.append(n3)
n3.neighbors.append(n2)
n3.neighbors.append(n4)
n4.neighbors.append(n1)
n4.neighbors.append(n3)
#result = S().cloneGraph(n1)


        
    


# https://www.youtube.com/watch?v=mQeF6bN8hMk&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=6&ab_channel=NeetCode

