graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start, visited=[]):
    visited.append(start)
    for next in graph[start] - set(visited):
        dfs(graph, next, visited)
    return visited

print(dfs(graph, 'C'))

