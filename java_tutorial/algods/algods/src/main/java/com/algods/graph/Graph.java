package com.algods.graph;

import java.util.HashSet;
import java.util.Set;

public interface Graph {

    boolean addVertex(Integer t);
    Double addEdge(Integer from, Integer to);
    boolean addEdge(Integer from, Integer to, Double weight);
    boolean removeVertex(Integer t);
    boolean removeEdge(Integer from, Integer to);
    Set<Integer> getVertices();
    HashSet<Object> getNeighbors(Integer ver);
    int size();
}
