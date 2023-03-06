package com.zetcode.app.collection;

import java.util.LinkedList;

public class LinkedListEx {
    public static void main(String[] args) {

        LinkedList<Integer> nums = new LinkedList<>();

        nums.add(5);
        nums.add(10);
        nums.add(13);
        nums.add(12);
        nums.add(15);
        nums.add(23);

        System.out.println(nums);

        nums.removeFirst();
        nums.removeLast();
        nums.addFirst(17);
        nums.addLast(77);

        System.out.println(nums);
    }
}
