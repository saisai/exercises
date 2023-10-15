package com.mycompany.leetcode.blind75.tree.ImplementTriePrefixTree;

public class ImplementTriePrefixTreeDeleted_user {
    class Node {
        Node[] nodes;
        boolean isEnd;

        Node() {
            nodes = new Node[26];
        }

        private void insert(String word, int idx) {
            if(idx >= word.length()) return;
            int i = word.charAt(idx) - 'a';
            if(nodes[i] == null) {
                nodes[i] = new Node();
            }

            if(idx == word.length() - 1) nodes[i].isEnd = true;
            nodes[i].insert(word, idx+1);
        }

        private boolean search(String word, int idx) {
            if(idx >= word.length()) return false;
            Node node = nodes[word.charAt(idx) - 'a'];
            if(node == null) return false;
            if(idx == word.length() - 1 && node.isEnd) return true;

            return node.search(word, idx+ 1);
        }

        private boolean startsWith(String prefix, int idx) {
            if(idx >= prefix.length()) return false;
            Node node = nodes[prefix.charAt(idx) - 'a'];
            if(node == null) return false;
            if(idx == prefix.length() - 1) return true;

            return node.startsWith(prefix, idx+1);
        }
    }

    Node root;

    public ImplementTriePrefixTreeDeleted_user() {
        root = new Node();
    }

    public void insert(String word) {
        root.insert(word, 0);
    }

    public boolean search(String word) {
        return root.search(word, 0);
    }

    public boolean startsWith(String prefix)  {
        return root.startsWith(prefix, 0);
    }

    public static void main(String[] args) {
        ImplementTriePrefixTreeDeleted_user trie = new ImplementTriePrefixTreeDeleted_user();
        trie.insert("apple");
        trie.search("apple");   // return True
        trie.search("app");     // return False
        trie.startsWith("app"); // return True
        trie.insert("app");
        trie.search("app");     // return True
    }

}
