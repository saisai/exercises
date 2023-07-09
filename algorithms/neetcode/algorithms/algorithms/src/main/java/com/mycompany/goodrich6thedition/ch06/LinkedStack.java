package com.mycompany.goodrich6thedition.ch06;

public class LinkedStack<E> implements Stack<E>{
    /**
     * The primary storage for elements of the stack
     */
    private SinglyLinkedList<E> list = new SinglyLinkedList<>();   // an empty list

    /**
     * Constructs an initially empty stack.
     */
    public LinkedStack() {
    }                   // new stack relies on the initially empty list

    @Override
    public int size() {
        return list.size();
    }

    @Override
    public boolean isEmpty() {
        return list.isEmpty();
    }

    @Override
    public void push(E e) {
        list.addLast(e);
    }

    @Override
    public E top() {
        return list.first();
    }

    @Override
    public E pop() {
        return list.removeFirst();
    }

    public String toString() {
        return list.toString();
    }
}
