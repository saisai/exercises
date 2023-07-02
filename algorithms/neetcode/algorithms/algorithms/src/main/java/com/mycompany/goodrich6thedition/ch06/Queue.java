package com.mycompany.goodrich6thedition.ch06;

public interface Queue<E> {

    int size();
    boolean isEmpty();
    void enqueue(E e);
    E first();
    E dequeue();
}
