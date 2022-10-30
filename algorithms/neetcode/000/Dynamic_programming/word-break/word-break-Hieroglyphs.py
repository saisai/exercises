'''
For BFS, DFS recursive with memo, and DP solutions, please visit the link below:
https://leetcode.com/problems/word-break/discuss/1326943/Python-Two-BFS-solutions-or-Explained-%2B-visualized

Trie Solution Idea:

Build your dictionary of words using a trie DS.
In the trie dictionary, every word is represented by a path from the root to a leaf (the root is a null node since its shared by all words in the dictionary)
Along every path, a word is stored as a series of nodes (aka linked list) where each node represents a character in the word (path)
The main building block of a trie is a node
The nodes have 3 basic attributes: value, children, a flag to indicate whether the
Time and space complexity:

add() O(K) where K = len(words)
find() O(S) where s = sentence
wordBreak() O(W * K) OR O(S * S[i+1:]) Whichever is worst, where W=len(words)

https://leetcode.com/problems/word-break/discuss/490911/Python-Simple-Trie-solution-with-detailed-explanation-and-sketches

https://leetcode.com/problems/word-break/
'''
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		# instantiate an empty trie 
        trie = Trie()
        # Iterate over words in dictionary and build trie one word at a time
        for word in wordDict:   #------ O(W) where W = len(words)
            trie.add(word)  #--------------- O(K) where K = len(word)
        print(trie.root.children)
        # Words have been added. Find if s is made up of words in the trie
        return trie.find(s)  # ---- Overall time : O(W*K) OR O(S*S[i+1:]) Whichever is worst

class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_done = False

class Trie:
    def __init__(self):
        self.root = Node(None)
        self.memo = {}

    def add(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = Node(char)
            root = root.children[char]   # -- on to the child - going one level down the tire branch/path
	    root.is_done = True    # -------------- To mark the end of a word.
		                                                # This is necessary to make the "word break" functionality possible) -- SEE SKETCH-1-
                                                        # s = "Ilovecats", wordDict = ["I", "love", "cats"]
                                                        # Marking last chars of each word is the only way for the trie to distinguish between the words and to seperate the words
                                                        # while building the trie and also searching the trie later on.

    def find(self, s):
        root = self.root
        for i, char in enumerate(s):
            if char not in root.children:   # [1] -- if char does not exist
                return False
            
            if root.children[char].is_done: # [2] --  if char does exit, but it's marked as the last char/leaf node --- 
			                                            # SEE NOTE #[2] FOR A DETAILED EXPLANATION

                if s[i+1:] not in self.memo:                  # -- (a) if the remaining part hasn't been seen before, then we need to check it -> call the function recursively
                    self.memo[s[i+1:]] = self.find(s[i+1:]) 

                if self.memo[s[i+1:]]:                        # -- (b) if remaining has been seen - return True (no need to check)
                    return True                                      # -- Having seen the "remaining part" before is possible if a word repeats in the sentence.
                                                                            # for example:
                                                                            # A man gotta do what a man gotta do
                                                                            # ex: s = "Amangottadowhatamangottado"
                                                                            # The words "man", "do", "gotta", and "a" repeats twice each
                                                                            # in such scenario, it's wise to use a memoization dict to speed things up - see sketch 3

            root = root.children[char]         # ----- move on to the child node - go one level down the branch
        
        return root.is_done                   # ----- Only return True if the last char in s is marked as leaf in the trie
                                                       # This is another way of saying - we have found every word in our given sentence "s" 
                
            
    
	 # NOTE 2
     # ------   
     # We need to capture leaf nodes because in a trie, words that have the same prefix
     # will appear as one word as long as they share the prefix and
     # will only start to diverge from one another at the first non-mutual letter/character
     # *please see sketch -2-*

     # Thus, if char exists and it's marked as a leaf node in the trie.
     # there's no way to make sure whether this leaf node is 
     # the GLOBAL leaf node of that path/branch or just a LOCAL leaf node

     # GLOBAL leaf node belongs represents the char that belongs
     # to the longest word of all the words that share the same prefix.
     # While LOCAL leaf node marks the end of a shorter word that shares the
     # same prefix with longer words, and thus -in reality- is not really a 
     # <proper> leaf node as far as the trie is concenred. As a result,
     # whenever we encounter a leaf, we need to make sure that there's
     # no remaining characters by checking s[i+1:]
     # if s[i+1: ] is not None -> this means the word we'are trying to find
     # extends beyond that initial leaf node that we encountered 
     # <there are more characters to the word>, hence we need to call the function again
     # on that remaining part s[i+1: ] to make sure that it exists in the trie.
     # This makes sense becasue, so far we were able to find only the first part
     # s[:i] and we're sure it exists but we still have to verify the existence of
     # the remaing part. We do that by simply calling the function again -recursively-
     # on that remaining part.


'''

class S:

    def wordBreak(self, s, wordDict):
        
        trie = Trie()

        for word in wordDict:
            trie.add(word)
        print(trie.root.children)

        return trie.find(s)

class Node:

    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_done = False

class Trie:

    def __init__(self):
        self.root = Node(None)
        self.memo = {}

    def add(self, word):
        root = self.root
        for  char in word:
            if char not in root.children:
                root.children[char] = Node(char)
            root = root.children[char]
        root.is_done = True

    def find(self, s):
        root = self.root
        for i, char in enumerate(s):
            if char not in root.children:
                return False

            if root.children[char].is_done:

                if s[i+1:] not in self.memo:
                    self.memo[s[i+1:]] = self.find(s[i+1:])

                if self.memo[s[i+1:]]:
                    return True


            
            root = root.children[char]
        return root.is_done


s = "leetcode"
wordDict = ["leet","code"]
print(S().wordBreak(s, wordDict))
