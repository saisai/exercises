
const { ListNode } = require('./ListNode');

const mergeTwoLists = (l1, l2) => {
  
  if(!l1) return l2;
  else if(!l2) return l1;
  else if(l1.val <= l2.val) {
    l1.next = mergeTwoLists(l1.next, l2);
    return l1;
  } else {
    l2.next = mergeTwoLists(l1, l2.next);
    return l2;
  }
  
};

const l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
const l2 = new ListNode(1, new ListNode(3, new ListNode(4)));

console.log(l1);

let result = mergeTwoLists(l1, l2);

console.log(result);

while(result != null) {
  console.log(result.val);
  const tmp = result.next;
  result = tmp;
}
