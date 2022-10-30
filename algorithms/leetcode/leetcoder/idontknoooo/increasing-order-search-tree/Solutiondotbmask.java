/*
 * https://leetcode.com/problems/increasing-order-search-tree/discuss/165870/Java-Simple-InOrder-Traversal-with-Explanation
 * https://leetcode.com/problems/increasing-order-search-tree/
 * 
 *  */

import java.util.Arrays;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) {this.val = val;}
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;

    }
}


class Solutiondotbmask{

    TreeNode prev =null, head = null;
    public static void main(String[] args){

        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(3);


        Solutiondotbmask S = new Solutiondotbmask();
        System.out.println(S.increasingBST(root));

    }

    public TreeNode increasingBST(TreeNode root) {
        if(root == null) return null;
        increasingBST(root.left);
        if(prev != null) {
            root.left=null; // we no longer need the left side of the node, so set it to null
            prev.right = root;
        }

        if(head==null) head=root; // record the most left node as it will be our root
        prev = root; // keep track of the prev node
        increasingBST(root.right);
        return head;
    }
}