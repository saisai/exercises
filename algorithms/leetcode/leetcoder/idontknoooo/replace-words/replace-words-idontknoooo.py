"""

https://leetcode.com/problems/replace-words/
https://leetcode.com/problems/replace-words/discuss/1561930/python-3-trie-variation-explanation

Explanation
Replace word with the shortest root of it in dictionary
Add every root from dictionary to a trie
Search prefix for each word in sentence
If a root is found, return root (this guarantees the shortest)
Else, return word itself
Implementation

"""
from typing import List

class TrieNode:

    def __init__(self):
        self.children = dict()
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def root_of(self, word):
        node, prefix = self.root, ''
        for c in word:
            if c not in node.children:
                return word
            prefix += c
            node = node.children[c]
            if node.is_word:
                return prefix
        return word


class S:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        return ' '.join([trie.root_of(word) for word in sentence.split(' ')])

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(S().replaceWords(dictionary, sentence))
