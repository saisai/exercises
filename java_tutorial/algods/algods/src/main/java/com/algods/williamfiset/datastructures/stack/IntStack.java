package com.algods.williamfiset.datastructures.stack;

public class IntStack implements Stack<Integer> {

    private int[] ar;
    private int pos = 0;

    // maxSize is the maximum number of items
    // that can be in the queue at any given time
    public IntStack(int maxSize) {
        ar = new int[maxSize];
    }

    // returns the number of elements inside the stack
    public int size() {
        return pos;
    }

    // return true/false on whether the stack is empty
    public boolean isEmpty() {
        return pos == 0;
    }

    // returns the element at the top of the stack
    @Override
    public Integer peek() {
        return ar[pos - 1];
    }

    // add an element to the top of the stack
    @Override
    public void push(Integer value) {
        ar[pos++] = value;
    }

    // make sure you check that the stack is not empty before calling pop!
    @Override
    public Integer pop() {
        return ar[--pos];
    }

    // Example usage
    public static void main(String[] args) {

        IntStack s = new IntStack(5);

        s.push(1);
        s.push(2);
        s.push(3);
        s.push(4);
        s.push(5);

        System.out.println(s.pop()); // 5
        System.out.println(s.pop()); // 4
        System.out.println(s.pop()); // 3

        s.push(3);
        s.push(4);
        s.push(5);

        while (!s.isEmpty()) System.out.println(s.pop());

        //benchMarkTest();
    }
}
