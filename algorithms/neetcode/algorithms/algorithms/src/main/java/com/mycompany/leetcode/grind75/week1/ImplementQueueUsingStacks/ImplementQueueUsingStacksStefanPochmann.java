package com.mycompany.leetcode.grind75.week1.ImplementQueueUsingStacks;

import java.util.Stack;

public class ImplementQueueUsingStacksStefanPochmann {
    static class MyQueue {

        Stack<Integer> input = new Stack();
        Stack<Integer> output = new Stack();

        public void push(int x) {
            input.push(x);
        }

        public void pop() {
            peek();
            output.pop();
        }

        public int peek() {
            if (output.empty())
                while (!input.empty())
                    output.push(input.pop());
            return output.peek();
        }

        public boolean empty() {
            return input.empty() && output.empty();
        }
    }

    public static void main(String[] args) {
        MyQueue myQueue = new MyQueue();
        myQueue.push(1); // queue is: [1]
        myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
        myQueue.peek(); // return 1
        myQueue.pop(); // return 1, queue is [2]
        myQueue.empty(); // return false
    }
}
