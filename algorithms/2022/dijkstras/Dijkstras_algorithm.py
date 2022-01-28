from collections import namedtuple, deque
from pprint import pprint as pp

inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])

class Graph:

    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        #pp(dir(self.edges))
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}


    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
            neighbours[end].add((start, cost))

        #pp(neighbours)


        while q:

            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u

        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s

graph = Graph([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
               ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
               ("e", "f", 9)])
pp(graph.dijkstra("a", "e"))

for d in graph.dijkstra("a", "e"):
    print(d)


# http://rosettacode.org/wiki/Dijkstra%27s_algorithm#Python
