package com.mycompany.leetcode.TopInterview150.GraphGeneral.CloneGraph;

import com.mycompany.leetcode.TopInterview150.GraphGeneral.Nodes;

import java.util.HashMap;
import java.util.Map;

public class CloneGraph150doocs {
    private Map<Nodes, Nodes> visited = new HashMap<>();

    public Nodes cloneGraph(Nodes node) {
        if (node == null) {
            return null;
        }
        if (visited.containsKey(node)) {
            return visited.get(node);
        }
        Nodes clone = new Nodes(node.val);
        visited.put(node, clone);

        for (Nodes e : node.neighbors) {
            clone.neighbors.add(cloneGraph(e));
        }
        return clone;
    }

    public static void main(String[] args) {
        Nodes node1 = new Nodes(1);
        Nodes node2 = new Nodes(2);
        Nodes node3 = new Nodes(3);
        Nodes node4 = new Nodes(4);

        node1.neighbors.add(node2);
        node1.neighbors.add(node4);

        node2.neighbors.add(node1);
        node2.neighbors.add(node3);

        node3.neighbors.add(node2);
        node3.neighbors.add(node4);

        node4.neighbors.add(node1);
        node4.neighbors.add(node3);

        CloneGraph150doocs obj = new CloneGraph150doocs();
        Nodes result = obj.cloneGraph(node1);
        printGraph(result, new HashMap<>());

    }

    private static void printGraph(Nodes origin, Map<Integer, Nodes> used) {

        if (!used.containsKey(origin.val)) {
            System.out.println(origin.val);

            used.put(origin.val, origin);
            for (int i = 0; i < origin.neighbors.size(); i++) {
                printGraph(origin.neighbors.get(i), used);
            }
        }
    }

}

// https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0133.Clone%20Graph/README_EN.md
