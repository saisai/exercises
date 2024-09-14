
import { TreeNode } from './treenode.js'

const lowestCommonAncestor  = (root, p, q) => {
  if(root.val < p.val && root.val < q.val) {
    return lowestCommonAncestor(root.right, p, q);
  }

  if(root.val > p.val && root.val > q.val) {
    return lowestCommonAncestor(root.left, p, q);
  }
  return root;
}

let root = new TreeNode(6);
root.left = new TreeNode(2, new TreeNode(0), new TreeNode(4, new TreeNode(3), new TreeNode(5)));
root.right = new TreeNode(8, new TreeNode(7), new TreeNode(9));

console.log(root);

let p = new TreeNode(2);
let q = new  TreeNode(8);
let result = lowestCommonAncestor(root, p, q);
console.log(result);

