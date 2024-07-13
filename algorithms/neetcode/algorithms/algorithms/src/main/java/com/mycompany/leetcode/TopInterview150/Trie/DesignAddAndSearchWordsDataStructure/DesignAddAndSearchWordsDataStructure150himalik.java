package com.mycompany.leetcode.TopInterview150.Trie.DesignAddAndSearchWordsDataStructure;

public class DesignAddAndSearchWordsDataStructure150himalik {
    private DesignAddAndSearchWordsDataStructure150himalik[] children;
    boolean isEndOfWord;

    public DesignAddAndSearchWordsDataStructure150himalik() {
        children = new DesignAddAndSearchWordsDataStructure150himalik[26];
        isEndOfWord = false;
    }

    public void addWord(String word) {
        DesignAddAndSearchWordsDataStructure150himalik curr = this;
        for(char c : word.toCharArray()) {
            if(curr.children[c - 'a'] == null)
                curr.children[c - 'a'] =  new DesignAddAndSearchWordsDataStructure150himalik();
            curr = curr.children[c - 'a'];
        }
        curr.isEndOfWord = true;
    }

    public boolean search(String word) {
        DesignAddAndSearchWordsDataStructure150himalik curr = this;
        for(int i = 0; i < word.length(); ++i) {
            char c = word.charAt(i);
            if(c == '.') {
                for(DesignAddAndSearchWordsDataStructure150himalik ch : curr.children)
                    if(ch != null && ch.search(word.substring(i + 1))) return true;
                return false;
            }
            if(curr.children[c - 'a'] == null) return false;
            curr = curr.children[c - 'a'];
        }
        return curr != null && curr.isEndOfWord;
    }

    public static void main(String[] args) {
        DesignAddAndSearchWordsDataStructure150himalik wordDictionary = new DesignAddAndSearchWordsDataStructure150himalik();

        wordDictionary.addWord("bad");
        wordDictionary.addWord("dad");
        wordDictionary.addWord("mad");
        wordDictionary.search("pad"); // return False
        wordDictionary.search("bad"); // return True
        wordDictionary.search(".ad"); // return True
        wordDictionary.search("b.."); // return True
    }
}
