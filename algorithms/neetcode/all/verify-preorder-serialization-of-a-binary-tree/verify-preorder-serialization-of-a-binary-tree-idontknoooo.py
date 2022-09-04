

class S:

    def isValidSerialization(self, preorder: str) -> bool:

        preorder = preorder.split(',')
        n = len(preorder)
        idx, enough = 0, True # static `idx`, `enough` node to build a binary tree
        def dfs():
            nonlocal n, idx, enough
            if idx >= n: enough = False; return # if not enough node to build a binary tree
            if preorder[idx] == '#': return
            if preorder[idx] != '#':
                idx += 1    # say this is `idx_1`
                dfs()       # build left tree
                idx += 1    # now, `idx` is not `idx_1 + 1` because `idx` is static and it's increasing during recursion, Hope this solve your confusion
                dfs()       # build right tree

        dfs()
        return enough and idx >= n - 1 # all characters are visited and they are enough to build a tree

preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(S().isValidSerialization(preorder))
