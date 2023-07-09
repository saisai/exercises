package com.mycompany.goodrich6thedition.ch07;

import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.function.Consumer;

public class LinkedPositionalList<E> implements PositionalList<E>, Iterable<E>{
    private class PositionIterator implements Iterator<Position<E>> {
        private Position<E> cursor = first();
        private Position<E> recent = null;

        @Override
        public boolean hasNext() {
            return (cursor != null);
        }

        @Override
        public Position<E> next() throws NoSuchElementException {
            if(cursor == null) throw new NoSuchElementException("nothing left");
            recent = cursor;
            cursor = after(cursor);
            return recent;
        }

        @Override
        public void remove() throws IllegalStateException {
            if (recent == null) throw new IllegalStateException("nothing left");
            LinkedPositionalList.this.remove(recent);
            recent = null; // do not all remove again until next called
        }
    }

    private class PositionIterable implements Iterable<Position<E>> {
        @Override
        public Iterator<Position<E>> iterator() {
            return new PositionIterator();
        }
    }

    @Override
    public Iterable<Position<E>> positions() {
        return new PositionIterable();
    }

    private class ElementIterator implements Iterator<E> {
        Iterator<Position<E>> posIterator = new PositionIterator();

        @Override
        public void remove() {
            posIterator.remove();
        }

        @Override
        public boolean hasNext() {
            return posIterator.hasNext();
        }

        @Override
        public E next() {
            return posIterator.next().getElement();
        }
    }

    @Override
    public Iterator<E> iterator() {
        return new ElementIterator();
    }

    private static class Node<E> implements Position<E> {
        private E element;
        private Node<E> prev;
        private Node<E> next;
        public Node(E e, Node<E> p, Node<E> n) {
            element = e;
            prev = p;
            next = n;
        }

        public E getElement() throws IllegalStateException {
            if (next == null) // convention for defunct node.
                throw new IllegalStateException("Position no longer valid.");
            return element;
        }

        public Node<E> getPrev() {
            return prev;
        }

        public Node<E> getNext() {
            return next;
        }

        public void setElement(E e) {
            element = e;
        }

        public void setPrev(Node<E> p) {
            prev = p;
        }

        public void setNext(Node<E> n) {
            next = n;
        }
    }

    // instance variables
    private Node<E> header;
    private Node<E> trailer;
    private int size = 0;

    public LinkedPositionalList() {
        header = new Node<>(null, null, null);
        trailer = new Node<>(null, header, null);
        header.setNext(trailer);
    }

    private Node<E> validate(Position<E> p) throws IllegalArgumentException {
        if (!(p instanceof Node)) throw new IllegalArgumentException("Invalid p");
        Node<E> node = (Node<E>) p;  // safe cast
        if (node.getNext() == null)  // convention for defunct node
            throw new IllegalArgumentException("p is no longer in the list");
        return node;
    }

    /**
     * Returns the given node as a Position (or null, if it is a sentinel).
     *
     * @param node
     * @return
     */
    private Position<E> position(Node<E> node) {
        if (node == header || node == trailer)
            return null;
        return node;
    }

    // public accessor methods

    /**
     * @return the number of element in the linked list.
     */
    @Override
    public int size() {
        return size;
    }

    /**
     * Tests whether the linked list is empty.
     */
    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Returns the first Position in the linked list (or null, if empty)
     */
    @Override
    public Position<E> first() {
        return position(header.getNext());
    }

    /**
     * Return the last Position in the linked list (or null, if empty).
     */
    @Override
    public Position<E> last() {
        return position(trailer.getPrev());
    }

    /**
     * Returns the Position immediately before Position p (or null, if p is first).
     *
     * @param p position
     * @return the Position before Position p
     * @throws IllegalArgumentException if Position invalid
     */
    @Override
    public Position<E> before(Position<E> p) throws IllegalArgumentException {
        Node<E> node = validate(p);
        return position(node.getPrev());
    }

    /**
     * Returns the Position immediately after Position p (or null, if p is last).
     *
     * @param p position
     * @return the Position after Position p
     * @throws IllegalArgumentException if Position invalid
     */
    @Override
    public Position<E> after(Position<E> p) throws IllegalArgumentException {
        Node<E> node = validate(p);
        return position(node.getNext());
    }

    //private utilities

    /**
     * Adds element e to the linked list between the given nodes.
     */
    private Position<E> addBetween(E e, Node<E> pred, Node<E> succ) {
        Node<E> newest = new Node<>(e, pred, succ); // create and link a new node
        pred.setNext(newest);
        succ.setPrev(newest);
        size++;
        return newest;
    }


    // public update methods

    /**
     * Inserts element e at the front of the linked list and returns its new Position
     *
     * @param e the element to be added.
     * @return its new Position
     */
    @Override
    public Position<E> addFirst(E e) {
        return addBetween(e, header, header.getNext());  // just after the header
    }

    /**
     * Inserts element e at the back of the linked list and returns its new Position
     *
     * @param e the element to be added.
     * @return its new Position
     */
    @Override
    public Position<E> addLast(E e) {
        return addBetween(e, trailer.getPrev(), trailer);  // just before the trailer
    }

    /**
     * Inserts element e immediately before Position p, and returns its new Position
     *
     * @param p the Position
     * @param e the element to be added
     * @return its new Position
     * @throws IllegalArgumentException if the Position invalid
     */
    @Override
    public Position<E> addBefore(Position<E> p, E e) throws IllegalArgumentException {
        Node<E> node = validate(p);
        return addBetween(e, node.getPrev(), node);
    }

    /**
     * Inserts element e immediately after Position p, and returns its new Position
     *
     * @param p the Position
     * @param e the element to be added
     * @return its new Position
     * @throws IllegalArgumentException if the Position invalid
     */
    @Override
    public Position<E> addAfter(Position<E> p, E e) throws IllegalArgumentException {
        Node<E> node = validate(p);
        return addBetween(e, node, node.getNext());
    }

    /**
     * Replaces the element stored at Position p and returns the replaced element.
     *
     * @param p the position
     * @param e the new element at Position p
     * @return the replaced element
     * @throws IllegalArgumentException if the Position invalid
     */
    @Override
    public E set(Position<E> p, E e) throws IllegalArgumentException {
        Node<E> node = validate(p);
        E answer = node.getElement();
        node.setElement(e);
        return answer;
    }

    /**
     * Removes the element stored at Position p and returns it (invalidating p).
     *
     * @param p the position in which the element to be removed
     * @return the removed element at Position p
     * @throws IllegalArgumentException if the Position invalid
     */
    @Override
    public E remove(Position<E> p) throws IllegalArgumentException {
        Node<E> node = validate(p);
        Node<E> predecessor = node.getPrev();
        Node<E> successor = node.getNext();
        predecessor.setNext(successor);
        successor.setPrev(predecessor);
        size--;
        E answer = node.getElement();
        node.setElement(null);  // help with garbage collection
        node.setNext(null);     // and convention for defunct node
        node.setPrev(null);
        return answer;
    }
}
