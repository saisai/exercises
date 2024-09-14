
const { ListNode } = require('./ListNode');

const reverseList = (head) => {
  let [prev, current] = [null, head];
  while(current) {
    [current.next, prev, current] = [prev, current, current.next];
  }
  return prev;
}

//const head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));


var head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(4, new ListNode(5));

//console.log(head);

const result = reverseList(head);

//console.log(result);


while(result !== null) {
  console.log(result.val);
  var tmp = new ListNode();
  tmp = result.next;
  result = tmp;
}
