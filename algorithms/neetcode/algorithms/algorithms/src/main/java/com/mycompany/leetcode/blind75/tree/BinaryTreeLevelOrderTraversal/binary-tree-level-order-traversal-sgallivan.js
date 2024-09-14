
import { TreeNode } from './treenode.js'

const levelOrder = (root) => {
  
  let q = [root], ans = [];
  while(q[0]) {
    let qlen = q.length, row = [];
    for(let i = 0; i < qlen; i++) {
      let curr = q.shift();
      row.push(curr.val);
      if(curr.left) q.push(curr.left)
      if(curr.right) q.push(curr.right)
    }
    ans.push(row)
  }
  return ans;
}

const root = new TreeNode(3, new TreeNode(9));
root.right = new TreeNode(20, new TreeNode(15), new TreeNode(7));

console.log(root);


console.log(levelOrder(root));
