package com.mycompany.goodrich6thedition.ch08;

import com.mycompany.goodrich6thedition.ch07.Position;

public interface BinaryTree<E> extends Tree<E> {
    Position<E> left(Position<E> p) throws IllegalArgumentException;
    Position<E> right(Position<E> p) throws IllegalArgumentException;
    Position<E> sibling(Position<E> p) throws IllegalArgumentException;
}
