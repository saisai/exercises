
const { ListNode } = require('./ListNode');

const mergeKLists = lists => {
  const dummyHead = new ListNode();
  let curr = dummyHead;

  const findMin = arr => {
    let min = Infinity;

    for(let node of arr) {
      if(!node) continue;
      min = Math.min(min, node.val);
    }

    return min;
  };

  while(true) {
    const min = findMin(lists);
    if(min === Infinity) return dummyHead.next;

    for(let i = 0; i < lists.length; i++) {
      if(!lists[i] || lists[i].val > min) continue;;
      curr.next = lists[i];
      curr = curr.next;
      lists[i] = lists[i].next;
    }
  }
}


const a = new ListNode(1, new ListNode(4, new ListNode(5)));
const b = new ListNode(1, new ListNode(3, new ListNode(4)));
const c = new ListNode(2, new ListNode(5));

let lists = [a, b, c];

let listss= mergeKLists(lists);

while(listss != null) {
  console.log(listss.val);
  const tmp = listss.next;
  listss = tmp;
}

