package com.mycompany.goodrich6thedition.ch06;

public interface Deque<E> {
    int size();
    boolean isEmpty();
    E first();

    E last();

    void addFirst(E e);
    void addLast(E e);
    E removeFirst();
    E removeLast();
}
