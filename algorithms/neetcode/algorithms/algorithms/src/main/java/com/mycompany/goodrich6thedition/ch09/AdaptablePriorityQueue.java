package com.mycompany.goodrich6thedition.ch09;

public interface AdaptablePriorityQueue<K, V> extends PriorityQueue<K, V> {
    /**
     * Removes the given entry from the priority queue.
     *
     * @param entry an entry of this priority queue
     * @throws IllegalArgumentException if e is not a valid entry for the priority queue.
     */
    void remove(Entry<K, V> entry) throws IllegalArgumentException;

    /**
     * Replaces the key of an entry.
     *
     * @param entry an entry of this priority queue
     * @param key   the new key
     * @throws IllegalArgumentException if e is not a valid entry for the priority queue.
     */
    void replaceKey(Entry<K, V> entry, K key) throws IllegalArgumentException;

    /**
     * Replaces the value of an entry.
     *
     * @param entry an entry of this priority queue
     * @param value the new value
     * @throws IllegalArgumentException if e is not a valid entry for the priority queue.
     */
    void replaceValue(Entry<K, V> entry, V value) throws IllegalArgumentException;
}
