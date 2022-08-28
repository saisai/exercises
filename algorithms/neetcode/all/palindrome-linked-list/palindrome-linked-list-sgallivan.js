/*
 * https://leetcode.com/problems/palindrome-linked-list/
 *https://leetcode.com/problems/palindrome-linked-list/discuss/1137027/JS-Python-Java-C%2B%2B-or-Easy-Floyd's-%2B-Reversal-Solution-w-Explanation

 */
function ListNode(val, next) {
	this.val = (val===undefined ? 0 : val)
	this.next = (next===undefined ? null : next)
}


var isPalindrome = function(head){
	let slow = head, fast = head, prev, temp
	while(fast && fast.next)
		slow = slow.next, fast = fast.next.next
	prev = slow, slow = slow.next, prev.next = null
	while(slow)
		temp = slow.next, slow.next = prev, prev = slow, slow = temp
	fast = head, slow = prev
	while(slow)
		if(fast.val !== slow.val) return false
		else fast = fast.next, slow = slow.next
	return true
}

let head = new ListNode(1)
head.next = new ListNode(2)
head.next.next = new ListNode(2)
head.next.next.next = new ListNode(1)

console.log(head)
const root = head
while(head){
	console.log(head.val)
	head = head.next
}

console.log(isPalindrome(root))

