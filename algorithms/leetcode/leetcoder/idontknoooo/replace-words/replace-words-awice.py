'''
https://leetcode.com/problems/replace-words/discuss/105755/Python-Straightforward-with-Explanation-(Prefix-hash-Trie-solutions)
https://leetcode.com/problems/replace-words/

'''
class S:
    def replaceWords(self, roots, sentence):

        rootset = set(roots)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(S().replaceWords(dictionary, sentence))
