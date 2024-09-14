
import { TreeNode } from "./treenode.js"

const maxPathSum = (root) => {
  let max = -Infinity;

  const findSums = (node) => {
    // Base case / hit a null

    if(!node) return 0;

    let left = findSums(node.left),
      right = findSums(node.right),
      allSum = left + right + node.val,
      leftNodeSum = left + node.val,
      rightNodeSum = right + node.val;

    // Max is all possible combinations
    max = Math.max(max, node.val, allSum, leftNodeSum, rightNodeSum);

    // Return the MAX path, which can be node.val, left + node.val or right + node.val
    return Math.max(leftNodeSum, rightNodeSum, node.val);
  };

  findSums(root);

  return max;

}

var root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);

console.log(maxPathSum(root));
