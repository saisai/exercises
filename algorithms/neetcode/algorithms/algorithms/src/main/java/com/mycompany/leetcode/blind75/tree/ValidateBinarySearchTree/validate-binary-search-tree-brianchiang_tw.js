
import { TreeNode } from "./treenode.js";

const validate = (node, lower, upper) => {
  if(node == null) {
    // empty node or empty tree
    return true;
  }

  if((lower < node.val) && (node.val < upper)) {
    // check if all tree nodes following BST rule
    return validate(node.left, lower, node.val) && validate(node.right, node.val, upper);
  } else {
    // early reject when we find vilation
    return false;
  }
}


const isValidBST = (root) => {
  return validate(root, -Infinity, Infinity);
}


const root = new TreeNode(2, new TreeNode(1), new TreeNode(3));

console.log(root);

const result = isValidBST(root);

console.log(result);

