from collections import deque, defaultdict

class S:

    def ladderLength(self, beginWord, endWord, wordList):

        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        print(nei)

        words = []
        visit = set([beginWord])
        print(visit)
        q = deque([beginWord])
        print(q)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(S().ladderLength(beginWord, endWord, wordList))

# https://www.youtube.com/watch?v=h9iTnkgv05E&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=7&ab_channel=NeetCode
