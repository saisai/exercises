

const  {ListNode}  = require('./ListNode');

const reorderList = head => {
  let stack = [], node = head;
  if(!node) return
  while(node) {
    stack.push(node);
    node = node.next;
  }

  let len = stack.length;
  node = head;
  for(let i = 0; i < len; i++) {
    if(i % 2 === 0)
      node.next = stack.shift()
    else
      node.next = stack.pop()
    node = node.next
  }
  node.next = null;
};


let head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));

reorderList(head);

while(head) {
  console.log(head.val);
  const tmp = head.next
  head =  tmp;
}
