package com.mycompany.goodrich6thedition.ch07;

public interface Position<E> {
    E getElement() throws IllegalStateException;
}
