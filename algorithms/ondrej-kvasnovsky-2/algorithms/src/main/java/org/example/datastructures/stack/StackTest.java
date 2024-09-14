package org.example.datastructures.stack;

class MyStackNode {
    int val;

    MyStackNode next;

    public MyStackNode(int val) {
        this.val = val;
    }
}

class MyStack {
    MyStackNode head;

    void push(int i) {
        MyStackNode n = new MyStackNode(i);
        if(head == null) {
            head = n;
        } else {
            n.next = head;
            head = n;
        }
    }

    int poll() {
        if(head == null) return -1;
        else {
            int val = head.val;
            head = head.next;
            return val;
        }
    }
}
public class StackTest {
    public static void main(String[] args) {
        MyStack stack = new MyStack();
        stack.push(1);
        stack.push(2);
        System.out.println(stack.poll()); // 2
        stack.push(3);
        System.out.println(stack.poll()); // 3
        System.out.println(stack.poll()); // 1
    }
}

// https://ondrej-kvasnovsky-2.gitbook.io/algorithms/data-structures/stack
