package com.mycompany.goodrich6thedition.ch06;

public interface Stack<E>{

    int size();
    boolean isEmpty();
    void push(E e);
    E top();
    E pop();

}
