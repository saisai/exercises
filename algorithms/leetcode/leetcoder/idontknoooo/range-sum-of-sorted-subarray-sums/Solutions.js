/*
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/1179733/JavaScript-O(N-logN)-Time-Using-Min-Heap
*/
import {
  
    MinPriorityQueue

   
  } from '@datastructures-js/priority-queue';

var rangeSum = function(nums, n, left, right){

const heap = new MinPriorityQueue({priority: x => x[0]});
const mod = 10**9 + 7;
let result = 0;

for(let i = 0; i < n; i++){
    heap.enqueue([nums[i], i]);
}

for(let i=1; i <= right; i++) {
    const [sum, idx] = heap.dequeue().element;
    if(i >= left) result = (result + sum) % mod;
    // extend teh subarray if it's not at the last idx
    if(idx < n - 1) heap.enqueue([sum+nums[idx+1], idx+1]);
}
return result;
}
var nums = [1,2,3,4], n = 4, left = 1, right = 5;
let result = rangeSum(nums, n, left, right);
console.log(result);

