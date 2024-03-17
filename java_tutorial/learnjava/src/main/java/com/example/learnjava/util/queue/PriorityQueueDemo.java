package com.example.learnjava.util.queue;

import java.util.Iterator;
import java.util.PriorityQueue;

public class PriorityQueueDemo {
    public static void main(String[] args) {
        PriorityQueue<String> queue = new PriorityQueue<String>();
        queue.add("Amit");
        queue.add("Vjay");
        queue.add("Jai");
        queue.add("Rahul");
        System.out.println("head: " + queue.element());
        System.out.println("head: " + queue.peek());

        Iterator itr = queue.iterator();
        while(itr.hasNext()) {
            System.out.println(itr.next());
        }

        queue.remove();
        queue.poll();

        System.out.println("After removing two elements");
        Iterator<String> itr2 = queue.iterator();
        while(itr2.hasNext()) {
            System.out.println(itr2.next());
        }

    }
}


// https://dotnettutorials.net/lesson/queue-collections-in-java/