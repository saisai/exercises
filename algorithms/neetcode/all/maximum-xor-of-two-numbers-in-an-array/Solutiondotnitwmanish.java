/*
   https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
 * https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/solutions/1012860/java-trie-binary-tree-bit-manipulation/
 */

class Solutiondotnitwmanish {

    class TrieNode {
        TrieNode left, right;
        public TrieNode() {
            left = null;
            right = null;
        }
    }
    
    //Insert by iteration
    public void insert(TrieNode root, int num) {
        TrieNode curr = root;
        
        for(int i = 31; i >= 0; i--) {
            int bit = (num>>i) & 1;
            if(bit == 0) {
                if(curr.left == null) {
                    curr.left = new TrieNode();
                }
                curr = curr.left;
            } else {
                if(curr.right == null) {
                    curr.right = new TrieNode(); 
                }
                curr = curr.right;
            }
        }
    }
    
    public int getMaxXor(TrieNode root, int num) {
        TrieNode curr = root;
        int maxXor = 0;
        
        for(int i = 31; i >= 0; i--) {
            int bit = (num>>i) & 1;
            if(bit == 0) {
                if(curr.right != null) {
                    curr =  curr.right;
                    maxXor += (1<<i);
                } else {
                    curr = curr.left;
                }
            } else {
                if(curr.left != null) {
                    curr = curr.left;
                    maxXor += (1<<i);   //pow(2,i)
                } else {
                    curr = curr.right;
                }
            }
        }
        
        return maxXor;
    }
    
    public int findMaximumXOR(int[] nums) {
        TrieNode root = new TrieNode();
        int maxXor = Integer.MIN_VALUE;
        
        for(int num: nums) {
            insert(root, num);
        }
        
        for(int num: nums) {
            maxXor = Math.max(maxXor, getMaxXor(root, num));
        }
        
        return maxXor;
    }

    public static void main(String[] args){
        Solutiondotnitwmanish S = new Solutiondotnitwmanish();

        int[] nums = {3,10,5,25,2,8};
        System.out.println(S.findMaximumXOR(nums));
    }

}