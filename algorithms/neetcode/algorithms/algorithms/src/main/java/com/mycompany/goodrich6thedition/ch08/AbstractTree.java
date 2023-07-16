package com.mycompany.goodrich6thedition.ch08;

import com.mycompany.goodrich6thedition.ch06.LinkedQueue;
import com.mycompany.goodrich6thedition.ch06.Queue;
import com.mycompany.goodrich6thedition.ch07.Position;


import java.util.ArrayList;
import java.util.List;

public abstract class AbstractTree<E> implements Tree<E>{
    @Override
    public boolean isInternal(Position<E> p) throws IllegalArgumentException {
        return numChildren(p) > 0;
    }

    @Override
    public boolean isExternal(Position<E> p) throws IllegalArgumentException {
        return numChildren(p) == 0;
    }

    @Override
    public boolean isRoot(Position<E> p) throws IllegalArgumentException {
        return size()  == 0;
    }

    @Override
    public boolean isEmpty() {
        return size() == 0;
    }

    public int depth(Position<E> p) {
        if(isRoot(p))
            return 0;
        else
            return 1 + depth(parent(p));
    }

    private int heightBad() {
        int h = 0;
        for(Position<E> p : positions())
            if(isExternal(p))
                h = Math.max(h, depth(p));
        return h;
    }

    public int height(Position<E> p) {
        int h = 0;
        for(Position<E> c : children(p))
            h = Math.max(h, 1 + height(c));
        return h;
    }

    private void preorderSubtree(Position<E> p, List<Position<E>> snapshot) {
        snapshot.add(p);
        for(Position<E> c : children(p))
            preorderSubtree(c, snapshot);
    }

    public Iterable<Position<E>> preorder() {
        List<Position<E>> snapshot = new java.util.ArrayList<>();
        if(!isEmpty())
            preorderSubtree(root(), snapshot);
        return snapshot;
    }

    /**
     * Adds positions of the subtree rooted at Position p to the given snapshot.
     */
    private void postorderSubtree(Position<E> p, List<Position<E>> snapshot) {
        for (Position<E> c : children(p))
            postorderSubtree(c, snapshot);
        snapshot.add(p);  // for postorder, we add position p after exploring subtrees
    }

    /**
     * Returns an iterable collection of positions of the tree, reported in postorder.
     */
    public Iterable<Position<E>> postorder() {
        List<Position<E>> snapshot = new ArrayList<>();
        if (!isEmpty())
            postorderSubtree(root(), snapshot);  // fill the snapshot recursively
        return snapshot;
    }

    public Iterable<Position<E>> breadthfirst() {
        List<Position<E>> snapshot = new ArrayList<>();
        if (!isEmpty()) {
            Queue<Position<E>> fringe = new LinkedQueue<>();
            fringe.enqueue(root());  // start with the root
            while (!fringe.isEmpty()) {
                Position<E> p = fringe.dequeue();  // remove from front of the queue
                snapshot.add(p);  // report this position
                for (Position<E> c : children(p))
                    fringe.enqueue(c);  // add children to back of queue
            }
        }
        return snapshot;
    }
}
