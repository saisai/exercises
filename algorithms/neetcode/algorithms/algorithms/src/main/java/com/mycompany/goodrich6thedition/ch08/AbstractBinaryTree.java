package com.mycompany.goodrich6thedition.ch08;

import com.mycompany.goodrich6thedition.ch07.Position;

import java.util.ArrayList;
import java.util.List;

public abstract class AbstractBinaryTree<E> extends AbstractTree<E> implements BinaryTree<E> {
    @Override
    public Position<E> sibling(Position<E> p) throws IllegalArgumentException {
        Position<E> parent = parent(p);
        if(parent == null) return null;
        if(p == left(parent))
            return right(parent);
        else
            return left(parent);
    }

    @Override
    public int numChildren(Position<E> p) throws IllegalArgumentException {
        int count = 0;
        if(left(p) != null)
            count++;
        if(right(p) != null)
            count++;
        return count;
    }

    public Iterable<Position<E>> children(Position<E> p) {
        List<Position<E>> snapshot = new ArrayList<>(2);
        if(left(p) != null)
            snapshot.add(left(p));
        if(right(p) != null)
            snapshot.add(right(p));
        return snapshot;
    }

    private void inorderSubtree(Position<E> p, List<Position<E>> snapshot) {
        if (left(p) != null)
            inorderSubtree(left(p), snapshot);
        snapshot.add(p);
        if (right(p) != null)
            inorderSubtree(right(p), snapshot);
    }

    public Iterable<Position<E>> inorder() {
        List<Position<E>> snapshot = new ArrayList<>();
        if (!isEmpty())
            inorderSubtree(root(), snapshot);  // fill the snapshot recursively
        return snapshot;
    }

    @Override
    public Iterable<Position<E>> positions() {
        return inorder();
    }

}
