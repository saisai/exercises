package com.mycompany.leetcode.grind75.week2.FirstBadVersion;


public class FirstBadVersionChengZhang {
//    public int firstBadVersion(int n) {
//        int start = 1, end = n;
//        while(start < end) {
//            int mid = start + (end - start ) / 2;
//            if(!isBadVersion(mid)) start = mid + 1;
//            else end = mid;
//        }
//        return start;
//    }
    public static void main(String[] args) {
        firstBadVersion obj = new firstBadVersion();
        System.out.println(obj.firstBadVersion(5));

    }
}
