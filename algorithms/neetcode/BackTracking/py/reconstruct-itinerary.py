

class S:

    def __call__(self, tickets):

        adj = { src : [] for src, dst in tickets }

        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        print(tickets)
        print(adj)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res

print(S()([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))

# https://leetcode.com/problems/reconstruct-itinerary/
# https://www.youtube.com/watch?v=ZyB_gQ8vqGA&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=18&ab_channel=NeetCode