
const { ListNode } = require('./ListNode');

const hasCycle = (head) => {
  let fast = head;
  while(fast && fast.next) {
    head = head.next;
    fast = fast.next.next;
    if(head === fast) return true;
  }
  return false;
};


let head = new ListNode(3, new ListNode(2, new ListNode(0, new ListNode(-4))));

console.log(head);

while(head != null) {
  console.log(head.val);
  var tmp = head.next;
  head = tmp;
}

const result = hasCycle(head);

console.log(result);
