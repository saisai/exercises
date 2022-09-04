from pathlib import Path
import sys


links = [
    "https://leetcode.com/problems/substring-with-largest-variance/discuss/2042949/python-3-kadanes-algorithm-two-pointers-explanation",
    "https://leetcode.com/problems/is-graph-bipartite/discuss/1999283/python-3-dfs-bfs-explanation",
    "https://leetcode.com/problems/design-an-atm-machine/",
    "https://leetcode.com/problems/split-array-largest-sum/discuss/1899661/python-3-binary-search-explanation",
    "https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/2516754/python-3-brutal-force-10-lines-explanation",
        ]
link_dict = {
        'shifting-letters-ii': 'https://leetcode.com/problems/shifting-letters-ii/discuss/2492482/python-3-prefix-sum-explanation',
        'palindrome-linked-list': 'https://leetcode.com/problems/palindrome-linked-list/discuss/2466415/python-3-o1-space-explanation',
        'count-subarrays-with-score-less-than-k': 'https://leetcode.com/problems/count-subarrays-with-score-less-than-k/discuss/2140147/python-3-sliding-window-two-pointers-math-explanation',

        'successful-pairs-of-spells-and-potions': 'https://leetcode.com/problems/successful-pairs-of-spells-and-potions/discuss/2139547/python-3-math-binary-search-explanation',

        'top-k-frequent-words': 'https://leetcode.com/problems/top-k-frequent-words/discuss/2078298/python3-onlogk-heap-customized-string-explanation',
        'friends-of-appropriate-ages': "https://leetcode.com/problems/friends-of-appropriate-ages/discuss/2074946/python-3-three-methods-binary-search-counterhashmap-math-explanation",

        "substring-with-largest-variance": "https://leetcode.com/problems/substring-with-largest-variance/discuss/2042949/python-3-kadanes-algorithm-two-pointers-explanation",
        "is-graph-bipartite": "https://leetcode.com/problems/is-graph-bipartite/discuss/1999283/python-3-dfs-bfs-explanation",
        "design-an-atm-machine": "https://leetcode.com/problems/design-an-atm-machine/discuss/1957787/python-3-greedy-pre-authorize-explanation",
        "increasing-order-search-tree": "https://leetcode.com/problems/increasing-order-search-tree/discuss/1955004/python-3-iterative-in-order-traversal-explanation",
        "spiral-matrix": "https://leetcode.com/problems/spiral-matrix/discuss/1948758/python-3-in-place-greedy-explanation",
        "number-of-ways-to-select-buildings": "https://leetcode.com/problems/number-of-ways-to-select-buildings/discuss/1907871/python-3-prefix-suffix-sum-easy-to-understand-explanation",

        "find-triangular-sum-of-an-array": "https://leetcode.com/problems/find-triangular-sum-of-an-array/discuss/1907687/python-3-in-place-compression-explanation",

        "split-array-largest-sum": "https://leetcode.com/problems/split-array-largest-sum/discuss/1899661/python-3-binary-search-explanation",
        "replace-non-coprime-numbers-in-array":"https://leetcode.com/problems/replace-non-coprime-numbers-in-array",
        




        }

if __name__ == '__main__':
    argv = sys.argv[1]
    print(argv, type(argv))
    def listdirs(rootdir):
        for path in Path(rootdir).iterdir():
            if path.is_dir():
                if str(path) == argv:
                    print("already")
                listdirs(path)

    print(listdirs('.'))

    '''
    for link in links:
        if link == argv:
            print("already")
        else:
            print("no")
    '''

