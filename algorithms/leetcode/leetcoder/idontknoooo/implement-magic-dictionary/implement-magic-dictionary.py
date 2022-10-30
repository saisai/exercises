'''
https://leetcode.com/problems/implement-magic-dictionary/

https://leetcode.com/problems/implement-magic-dictionary/solutions/762222/python-3-standard-trie-dfs-with-explanation/
'''

from typing import List

class TrieNode:

    def __init__(self):
        self.children = dict()
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        def helper(node, word, mod):
            if mod < 0 or not word: return False
            if mod == 0 and len(word) == 1 and word[0] in node.children and node.children[word[0]].is_word: return True
            elif mod > 0 and len(word) == 1 and any([node.children[c].is_word for c in node.children if c != word[0]]): return True
            ans = False
            for c in node.children:
                if c == word[0]:
                    ans |= helper(node.children[c], word[1:], mod)
                else:
                    ans |= helper(node.children[c], word[1:], mod-1)
            return ans
        return helper(self.root, word, 1)


class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, words: List[str]) -> None:
        for word in words:
            self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)

magicDictionary = MagicDictionary()
magicDictionary.buildDict(["hello", "leetcode"])
magicDictionary.search("hello")
print(magicDictionary.search("hhllo"))
print(magicDictionary.search("hell"))
print(magicDictionary.search("leetcoded"))
