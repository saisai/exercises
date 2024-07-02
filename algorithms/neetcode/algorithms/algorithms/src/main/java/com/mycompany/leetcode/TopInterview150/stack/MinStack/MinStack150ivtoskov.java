package com.mycompany.leetcode.TopInterview150.stack.MinStack;

public class MinStack150ivtoskov {
    private class Node {
        int val;
        int min;
        Node next;
        private Node(int val, int min, Node next) {
            this.val = val;
            this.min = min;
            this.next = next;
        }
    }

    private Node head;

    public void push(int x) {
        if(head == null) {
            head = new Node(x, x, null);
        } else {
            head = new Node(x, Math.min(x, head.min), head);
        }
    }

    public void pop() {
        head = head.next;
    }

    public int top() {
        return head.val;
    }

    public int getMin() {
        return head.min;
    }

    public static void main(String[] args) {
        MinStack150ivtoskov minStack = new MinStack150ivtoskov();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin(); // return -3
        minStack.pop();
        minStack.top();    // return 0
        System.out.println(minStack.getMin()); // return -2

    }
}
