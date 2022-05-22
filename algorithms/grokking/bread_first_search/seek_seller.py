

from collections import deque

def person_is_seller(name):
    return name == "samir duran"

def bfs(name):

    if name not in graph:
        return None

    person_visited = set()
    queue = deque()
    queue += graph[name]

    while queue:
        person = queue.popleft()

        if person not in person_visited:
            if person_is_seller(person):
                print(person + " is seller")
                return person
            else:
                queue += graph[person]
                person_visited.add(person)
    return None


graph = {"me": ["zeratul", "kerrigan", "jim raynor"], "zeratul": ["artanis", "aldaris", "danimoth"],
         "kerrigan": ["jim raynor"], "jim raynor": ["aleksander", "samir duran"], "artanis": [], "aldaris": [],
         "danimoth": ["aldaris"], "aleksander": [], "samir duran": []}

bfs("me")


# https://github.com/ronelzb/grokking-algorithms/blob/master/06_breadth-first_search/01_seek_seller.py
