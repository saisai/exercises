package com.mycompany.leetcode.blind75.array.SearchInRotatedSortedArray;

public class SearchInRotatedSortedArrayYanginblack {
    public int search(int[] A, int target) {
        if (A.length == 0) return -1;
        int L =0, R = A.length - 1;

        if (target < A[L] && target > A[R]) return -1;

        while(L < R) {
            int M = (L +R ) / 2;
            if(A[M] <= A[R]) {
                if(target > A[M] && target <= A[R]) {
                    L = M + 1;
                } else {
                    R = M;
                }
            } else {
                if(target <= A[M] && target >= A[L]) {
                    R = M;
                } else {
                    L = M + 1;
                }
            }
        }
        if(A[L] == target) return L;
        else return -1;
    }

    public static void main(String[] args) {
        int[] nums = {4,5,6,7,0,1,2};
        int target = 0;
        SearchInRotatedSortedArrayYanginblack obj = new SearchInRotatedSortedArrayYanginblack();
        System.out.println(obj.search(nums, target));
    }
}


// https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/14659/binary-search-java-solusion-o-log-n/