package com.mycompany.leetcode.TopInterview150.Trie;

public class TrieNode {
    public char val;
    public boolean isWord;
    public TrieNode[] children = new TrieNode[26];
    public TrieNode() {}

    public TrieNode(char c) {
        TrieNode node = new TrieNode();
        node.val = c;
    }
}
