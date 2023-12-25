package com.mycompany.leetcode.grind75.week5.SearchInRotatedSortedArray;

public class SearchInRotatedSortedArrayJerry13466 {
    public int search(int[] A, int target) {
        int lo = 0;
        int hi = A.length - 1;
        while(lo < hi) {
            int mid = (lo + hi) / 2;
            if(A[mid] == target) return mid;
            if(A[lo] <= A[mid]) {
                if(target >= A[lo] && target < A[mid]) {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            } else {
                if (target > A[mid] && target <= A[hi]) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
        }
        return A[lo] == target ? lo : -1;
    }

    public static void main(String[] args) {
        int[] nums = {4,5,6,7,0,1,2};
        int target = 0;

        SearchInRotatedSortedArrayJerry13466 obj = new SearchInRotatedSortedArrayJerry13466();
        System.out.println(obj.search(nums, target));
    }
}
