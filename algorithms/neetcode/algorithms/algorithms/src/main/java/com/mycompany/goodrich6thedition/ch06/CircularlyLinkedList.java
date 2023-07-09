package com.mycompany.goodrich6thedition.ch06;

public class CircularlyLinkedList<E> {
    private static class Node<E> {
        private E element;
        private Node<E> next;
        public Node(E e, Node<E> n) {
            element = e;
            next = n;
        }
        public E getElement() {
            return element;
        }
        public Node<E> getNext() {
            return next;
        }

        public void setNext(Node<E> n) {
            next = n;
        }
    }

    // instance variables of the CircularlyLinkedList
    private Node<E> tail = null;  // we store tail (but not head)
    private int size = 0;  // number of nodes in the list

    public CircularlyLinkedList() { }  // constructors an initially empty list

    // access methods
    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public E first() {
        if(isEmpty()) {
            return null;
        }
        return tail.getNext().getElement();
    }

    public E last() {
        if(isEmpty()) {
            return null;
        }
        return tail.getElement();
    }

    public void rotate() {
        if(tail != null) {
            tail = tail.getNext();
        }
    }

    public void addFirst(E e) {
        if(size == 0) {
            tail = new Node<>(e, null);
            tail.setNext(tail);
        } else {
            Node<E> newest = new Node<>(e, tail.getNext());
            tail.setNext(newest);
        }
        size++;
    }

    public void addLast(E e) {
        addFirst(e);
        tail = tail.getNext();
    }


    public E removeFirst() {
        if(isEmpty()) {
            return null;
        }
        Node<E> head = tail.getNext();
        if(head == tail) {
            tail = null;
        } else {
            tail.setNext(head.getNext());
        }
        size--;
        return head.getElement();
    }

}
