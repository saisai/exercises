package com.algods.graph;

import java.util.Arrays;

public class TestUnidrectedGraph {

    public static void main(String... args) {
        UndirectedGraph unGrpah = new UndirectedGraph();
        unGrpah.addVertex(1);
        unGrpah.addVertex(2);
        unGrpah.addVertex(3);
        unGrpah.addVertex(4);
        unGrpah.addEdge(1,2);
        unGrpah.addEdge(2,3);
        unGrpah.addEdge(3,4);
        unGrpah.addEdge(4,1);

        System.out.println(unGrpah.size());
        System.out.println(Arrays.toString(unGrpah.getVertices().toArray(new Integer[0])));

    }
}
