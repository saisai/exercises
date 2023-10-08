
import { TreeNode } from './treenode.js';

const kthSmallest = (root, k) => {
  let vals = [];
  (function dfs(node) {
    if(vals.length != k) { // no need to keep going after reach k-th number
      if(node.left) dfs(node.left); // go to left first
      vals.push(node.val); // finished going left, now start adding values
      if(node.right) dfs(node.right); // if have right, go there and repeat process

    }  
  })(root) // IFFE Immediately Invoking Function Expression, starting from root.
  return vals[k - 1];
}


const root = new TreeNode(3, new TreeNode(1), new TreeNode(4));
root.left.right = new TreeNode(2);

console.log(root);

let k = 1;
let result = kthSmallest(root, k);

console.log(result);
