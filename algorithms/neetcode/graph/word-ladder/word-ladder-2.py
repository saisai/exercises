from collections import deque, defaultdict
import string

class S:
    def ladderLength(self, beginWord, endWord, wordList):
        word_list = set(wordList)
        print(word_list)
        seen = set()
        q = deque([(beginWord, 1)])
        print(q)
        while q:
            word, num_words = q.popleft()
            if word == endWord:
                print("num_words" ,num_words)
                return num_words
            for i in range(len(word)):
                for ch in string.ascii_lowercase:
                    next_word = word[:i] + ch + word[i + 1:]
                    if next_word in word_list and next_word not in seen:
                        seen.add(next_word)
                        q.append((next_word, num_words + 1))
        return 0
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(S().ladderLength(beginWord, endWord, wordList))

# https://leetcode.com/problems/word-ladder/discuss/1870464/Python-3-Solution-or-BFS-or-Visited
