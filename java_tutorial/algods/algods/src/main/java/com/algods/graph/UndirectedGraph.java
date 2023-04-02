package com.algods.graph;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class UndirectedGraph implements Graph{
    private Map<Integer, HashSet<Object>> vertexMap = new HashMap<>();

    @Override
    public boolean addVertex(Integer v) {
        vertexMap.put(v, new HashSet<>());
        return true;
    }

    @Override
    public Set<Integer> getVertices() {
        return new HashSet<>(vertexMap.keySet());
    }

    @Override
    public HashSet<Object> getNeighbors(Integer ver) {
        return vertexMap.get(ver);
    }

    @Override
    public Double addEdge(Integer v1, Integer v2) {
        if (!vertexMap.containsKey(v1)) return -1d;
        if (!vertexMap.containsKey(v2)) return -1d;
        vertexMap.get(v1).add(v2);
        vertexMap.get(v2).add(v1);
        return 0d;
    }
    @Override
    public boolean addEdge(Integer v1, Integer v2, Double weight) {
        // not supported
        // use weighted graph
        return false;
    }

    @Override
    public boolean removeVertex(Integer v) {
        return false;
    }

    @Override
    public boolean removeEdge(Integer v1, Integer v2) {
        return false;
    }

    @Override
    public int size() {
        return vertexMap.size();
    }
}
