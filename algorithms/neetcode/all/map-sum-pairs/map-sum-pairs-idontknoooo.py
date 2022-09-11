'''
https://leetcode.com/problems/map-sum-pairs/
https://leetcode.com/problems/map-sum-pairs/discuss/1561908/python-3-trie-variation-explanation

Explanation
    Instead of using the naive trie structure, adding a self.val to make trie path a prefix sum value
    Time: N is the length of word or prefix
        insert: O(N)
        startsWith: O(N)
Implementation

'''
import collections

class TrieNode:

    def __init__(self):
        self.children = dict()
        self.val = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word = collections.defaultdict(int)

    def insert(self, word: str, val: int) -> None:
        word_val = self.word[word]
        self.word[word] = val
        val -= word_val
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.val += val

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.val

class MapSum:
    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.startsWith(prefix)



m = MapSum()
m.insert("apple", 3)
print(m.sum("ap"))
m.insert("app", 2)
print(m.sum("ap"))

