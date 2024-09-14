const { ListNode } = require('./ListNode');

const removeNthFromEnd = (head, n) => {
  let fast = head, slow = head;
  for(let i = 0; i < n; i++) fast = fast.next
  if(!fast) return head.next;
  while(fast.next) fast = fast.next, slow = slow.next
  slow.next = slow.next.next
  return head;
};

const head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));

console.log(head);

const result = removeNthFromEnd(head, 2);

console.log(result);

