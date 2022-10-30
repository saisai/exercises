'''
https://leetcode.com/problems/replace-words/discuss/105755/Python-Straightforward-with-Explanation-(Prefix-hash-Trie-solutions)
https://leetcode.com/problems/replace-words/

'''

import collections
class S:
    def replaceWords(self, roots, sentence):

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()

        END = True
        for root in roots:
            cur = trie
            for letter in root:
                cur = cur[letter]
            cur[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur: break
                cur = cur[letter]
                if END in cur:
                    return cur[END]
            return word
        return " ".join(map(replace, sentence.split()))
    


dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(S().replaceWords(dictionary, sentence))
