
import { TreeNode } from "./treenode.js";

function isSameTree(p, q) {
  if(!p && !q) return true;
  if(!p || !q || p.val !== q.val) return false;

  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}

var p = new TreeNode(1);
p.left = new TreeNode(2);
p.right = new TreeNode(3);

var q = new TreeNode(1);
p.left = new TreeNode(2);
p.right = new TreeNode(3);

console.log(isSameTree(p, q));
