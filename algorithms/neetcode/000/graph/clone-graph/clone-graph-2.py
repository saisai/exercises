
class Node:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class S:
    def cloneGraph(self, node):
        def dfs(node, copied_node):
            # iterate node neighbors
            for n in node.neighbors:
                # check if neighbor was already copied
                if n.val not in self.val2copied_node:                                        
                    # create a copy of curret node
                    copied_neighbor = Node(n.val)                
                    self.val2copied_node[n.val] = copied_neighbor
                    
                    # start a dfs search from neighbor node
                    dfs(node=n, copied_node=copied_neighbor)                                    
                
                # add copied node to the neighbors list
                copied_node.neighbors.append(self.val2copied_node[n.val])
                
        if not node:
            return node
        
        # make a copy of the root node
        copied_root = Node(val=node.val, neighbors=[])
        
        # hashmap to map value to its copied node
        self.val2copied_node = {copied_root.val: copied_root}
        
        # start dfs from the node, update copied root as we progress
        dfs(node, copied_root)
        
        return copied_root


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

# https://leetcode.com/problems/clone-graph/discuss/1966633/Python-cool-DFS-solution-with-comments
