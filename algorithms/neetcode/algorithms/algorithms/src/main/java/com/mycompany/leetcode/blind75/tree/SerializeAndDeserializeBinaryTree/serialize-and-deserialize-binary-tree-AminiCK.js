
import { TreeNode } from './treenode.js';

const serializeBFS = (root) => {
  let stack = [], serialize = [];
  if(root == null) return [];
  stack.push(root);
  while(stack.length > 0) {
    let node = stack.shift();
    serialize.push(node?node.val: null);
    if(node != null) {
      stack.push(node.left);
      stack.push(node.right);
    }

  }
  return serialize;
}

const deserializeBFS = (data) => {
  if(data[0] == null) return null;
  let node = new TreeNode(data.shift());
  let stack = [node];
  while(stack.length > 0) {
    let node = stack.shift();
    let left = data.shift();
    let right = data.shift();
    node.left = (left == null) ? null : new TreeNode(left);
    node.right = (right== null) ? null : new TreeNode(right);
    if(node.left != null) stack.push(node.left);
    if(node.right != null) stack.push(node.right);
  }
  return node;
}


const root = new TreeNode(1, new TreeNode(2), new TreeNode(3, new TreeNode(4), new TreeNode(5)));

console.log(root);


const aa = serializeBFS(root);

console.log(aa);


const bb = deserializeBFS(aa);

console.log(bb);
