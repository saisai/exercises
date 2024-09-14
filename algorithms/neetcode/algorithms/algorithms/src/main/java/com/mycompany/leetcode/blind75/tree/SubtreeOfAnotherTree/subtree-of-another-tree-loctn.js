

import { TreeNode } from "./treenode.js"

const isSubtree = (s, t) => {
  if(!s) return !t;
  return isEqual(s, t) || isSubtree(s.left, t) || isSubtree(s.right, t);
}

const isEqual = (root1, root2) => {
  if(!root1 || !root2) return !root1 && !root2;
  if(root1.val !== root2.val) return false;
  return isEqual(root1.left, root2.left) && isEqual(root1.right, root2.right);
}

const root = new TreeNode(3, new TreeNode(4, new  TreeNode(1), new TreeNode(2)), new TreeNode(5));
const subRoot = new TreeNode(4, new TreeNode(1), new TreeNode(2));

console.log(root);
console.log(subRoot);


const result = isSubtree(root, subRoot);
console.log(result);
