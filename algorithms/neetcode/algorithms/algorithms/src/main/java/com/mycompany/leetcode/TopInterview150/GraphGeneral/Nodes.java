package com.mycompany.leetcode.TopInterview150.GraphGeneral;

import java.util.ArrayList;
import java.util.List;

public class Nodes {
    public int val;
    public List<Nodes> neighbors;
    public Nodes() {
        val = 0;
        neighbors = new ArrayList<Nodes>();
    }
    public Nodes(int _val) {
        val = _val;
        neighbors = new ArrayList<Nodes>();
    }
    public Nodes(int _val, ArrayList<Nodes> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}