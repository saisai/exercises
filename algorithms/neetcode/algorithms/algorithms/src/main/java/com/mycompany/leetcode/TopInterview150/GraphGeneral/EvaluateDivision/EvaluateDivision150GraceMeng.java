package com.mycompany.leetcode.TopInterview150.GraphGeneral.EvaluateDivision;

import java.util.*;

public class EvaluateDivision150GraceMeng {

    private double getPathWeight(String start, String end,
                                 Set<String> visited, Map<String, Map<String, Double>> graph) {

        /* Rejection case. */
        if (!graph.containsKey(start))
            return -1.0;

        /* Accepting case. */
        if (graph.get(start).containsKey(end))
            return graph.get(start).get(end);

        visited.add(start);
        for (Map.Entry<String, Double> neighbour : graph.get(start).entrySet()) {
            if (!visited.contains(neighbour.getKey())) {
                double productWeight = getPathWeight(neighbour.getKey(), end, visited, graph);
                if (productWeight != -1.0)
                    return neighbour.getValue() * productWeight;
            }
        }

        return -1.0;
    }

    private Map<String, Map<String, Double>> buildGraph(String[][] equations, double[] values) {
        Map<String, Map<String, Double>> graph = new HashMap<>();
        String u, v;

        for (int i = 0; i < equations.length; i++) {
            u = equations[i][0];
            v = equations[i][1];
            graph.putIfAbsent(u, new HashMap<>());
            graph.get(u).put(v, values[i]);
            graph.putIfAbsent(v, new HashMap<>());
            graph.get(v).put(u, 1 / values[i]);
        }

        return graph;
    }

    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {

        /* Build graph. */
        Map<String, Map<String, Double>> graph = buildGraph(equations, values);
        double[] result = new double[queries.length];

        for (int i = 0; i < queries.length; i++) {
            result[i] = getPathWeight(queries[i][0], queries[i][1], new HashSet<>(), graph);
        }

        return result;
    }

    public static void main(String[] args) {
        String[][] equations = {{"a","b"},{"b","c"}};
        double[] values = {2.0,3.0};
        String[][] queries = {{"a","c"},{"b","a"},{"a","e"},{"a","a"},{"x","x"}};

        EvaluateDivision150GraceMeng obj = new EvaluateDivision150GraceMeng();
        double[] results = obj.calcEquation(equations, values, queries);
        for(double d : results) {
            System.out.println(d);
        }
    }
}
